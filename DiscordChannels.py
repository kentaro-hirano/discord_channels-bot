import discord

client = discord.Client()

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        # botRoom = client.get_channel(936162560561020948)
        botRoom = client.get_channel(936183156095213608)
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [936114247589593092, 936118770798317588, 936133924151754802, 936142615332675614, 936142842240319549]

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けました！")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")

# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run("OTM2MTQ4OTI2NTYwNjAwMDk0.YfI-oA.Vdy2I8X2T5TvMT3nj5ZIqSTCqas")

# import discord

# client = discord.Client()

# # 起動時処理
# @client.event
# async def on_ready():
#     for channel in client.get_all_channels():
#         print("----------")
#         print("チャンネル名：" + str(channel.name))
#         print("チャンネルID：" + str(channel.id))
#         print("----------")

# # Botのトークンを指定（デベロッパーサイトで確認可能）
# client.run("OTM2MTQ4OTI2NTYwNjAwMDk0.YfI-oA.Vdy2I8X2T5TvMT3nj5ZIqSTCqas")