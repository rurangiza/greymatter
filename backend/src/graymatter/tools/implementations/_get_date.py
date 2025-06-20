from datetime import datetime

from graymatter.tools.tool import Tool


class GetDate(Tool):
    locale: str

    def resolve(self) -> str:
        return f"Today's date is {datetime.today()}"
