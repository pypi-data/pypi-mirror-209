from slack_sdk import (
    WebClient,
)

from slack_sdk.errors import (
    SlackApiError,
)

from .util import (
    format_time_cost,
    _format_dt,
)


from datetime import datetime

import time
import json
import os

class SlackClient:
    def __init__(self, token:str):
        self._token = token

    def _dump_file(self, output_path: str, discussions: []):
        if (not discussions) or len(discussions) == 0:
            return

        oldest_ts = float('inf')
        latest_ts = 0.0
        need_items = []
        for discussion in discussions:
            ts = discussion[0]['ts']
            f_ts = float(ts)
            if latest_ts < f_ts:
                latest_ts = f_ts
            if oldest_ts > f_ts:
                oldest_ts = f_ts
            if "subtype" in discussion[0].keys():
                subtype = discussion[0]['subtype']
                if subtype == "channel_join" or subtype == "channel_name":
                    continue
            need_items.append(discussion)

        ot = _format_dt(datetime.fromtimestamp(oldest_ts))
        lt = _format_dt(datetime.fromtimestamp(latest_ts))
        full_path = os.path.join(output_path, "{}_to_{}.json".format(ot, lt))
        with open(full_path, 'w', encoding='utf-8') as f:
            print("Dump {:d} threads to file {:s}".format(len(need_items), full_path))
            content = {
                "count": len(need_items),
                "oldest_ts": str(oldest_ts),
                "latest_ts": str(latest_ts),
                "oldest_datetime": ot,
                "latest_datetime": lt,
                "threads": need_items,
            }
            json.dump(obj=content, fp=f, indent=2)

    def _get_latest_ts(self, channel_folder: str):
        latest_ts = 0
        if not os.path.exists(channel_folder):
            return latest_ts

        for parent, dirnames, filenames in os.walk(channel_folder):
            if parent is channel_folder:
                for filename in filenames:
                    ext = os.path.splitext(filename)
                    if len(ext) != 2 or ext[1] != ".json":
                        continue
                    fullpath = os.path.join(parent, filename)
                    with open(fullpath, encoding='utf-8') as f:
                        content = json.load(f)
                        if "latest_ts" in content.keys():
                            ts = float(content["latest_ts"])
                            if ts > latest_ts:
                                latest_ts = ts

        return latest_ts

    def list_channels(self):
        try:
            client = WebClient(token=self._token)
            resp = client.conversations_list()
            if not resp.get("ok"):
                print("Failed to list channels, error code:", resp.status_code)
                return []

            return resp["channels"]
        except SlackApiError as e:
            print(e)

    def channel_info(self, channel_id: str):
        try:
            client = WebClient(token=self._token)
            resp = client.conversations_info(channel=channel_id)
            if not resp.get("ok"):
                print("Failed to get channel info, error code:", resp.status_code)
                return {}

            return resp["channel"]
        except SlackApiError as e:
            print(e)

    def send_message(self, msg:str, channel_name:str):
        try:
            client = WebClient(token=self._token)
            resp = client.chat_postMessage(channel=channel_name, text=msg)
            print(resp)
        except SlackApiError as e:
            print(e)

    def fetch_messages(self, channel_id:str, from_ts:str="0", to_ts:str=None):
        try:
            print("Fetch messages from channel_id={:s}, from_ts={}, to_ts={}".format(channel_id, from_ts, to_ts))

            client = WebClient(token=self._token)
            resp = client.conversations_history(channel=channel_id, limit=50, oldest=from_ts, latest=to_ts)
            if not resp.get("ok"):
                print("Failed to get conversation history, error code:", resp.status_code)

            messages = resp.get("messages")
            has_more = resp.get("has_more")
            print("Received discussion threads:", len(messages), "has more:", has_more)

            newest_ts = 0.0
            for k in range(len(messages)):
                ts = messages[k]['ts']
                print("get thread", ts)
                f_ts = float(ts)
                if newest_ts < f_ts:
                    newest_ts = f_ts

                time.sleep(1)
                try:
                    resp = client.conversations_replies(channel=channel_id, ts=ts, limit=200)
                    replies = resp.get("messages")
                    for reply in replies:
                        f_ts = float(messages[k]['ts'])
                        reply['datetime'] = _format_dt(datetime.fromtimestamp(f_ts))
                    messages[k] = replies
                except Exception as e:
                    print("Feailed to get replies, error:", e)

            if has_more:
                more_msgs = self.fetch_messages(channel_id=channel_id, from_ts=str(newest_ts), to_ts=to_ts)
                if more_msgs is not None:
                    messages.extend(more_msgs)
            return messages
        except Exception as e:
            print("Feailed to fetch messages, error:", e)

    def fetch_channels(self, output_path: str):
        start = time.time()
        channels = self.list_channels()
        for channel in channels:
            if not channel["is_channel"]:
                print("Not a channel:", channel["name"])
                continue
            if channel["is_private"]:
                print("Channel is private:", channel["name"])
                continue
            if not channel["is_member"]:
                print("Not a member of the channel:", channel["name"])
                continue

            print("Channel:", channel)
            channel_folder = os.path.join(output_path, channel["name"])
            latest_ts = self._get_latest_ts(channel_folder)

            messages = self.fetch_messages(channel_id=channel["id"], from_ts=str(latest_ts))

            os.makedirs(name=channel_folder, exist_ok=True)
            self._dump_file(channel_folder, messages)

        end = time.time()
        print("Fetch messages from {:d} channels, total time cost:{:s}"
              .format(len(channels), format_time_cost(end - start)))
