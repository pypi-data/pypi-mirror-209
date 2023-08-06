import asyncio

from enkanetwork import EnkaNetworkAPI
from enkanetwork.model import CharacterInfo

client = EnkaNetworkAPI(
    lang="th", user_agent="EnkaNetwork.py/1.4.0 (Dev mode)")


async def main():
    async with client:
        # data = await client.fetch_user(618285856, info=True)
        # print(data.owner.username)

        # Export to JSON
        data = await client.fetch_user(843715177)
        # exportjson = data.characters[0].dict()

        # # Load JSON
        # print(CharacterInfo.parse_obj(exportjson))
    

asyncio.run(main())
