from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI(title="Rubber Dictionary API", description="Tra cứu từ điển chuyên ngành cao su", version="1.0")

dictionary = {
    "6d/7": "cạo 6 ngày trong tuần, nghỉ ngày chủ nhật (six days in tapping followed by one day of tapping rest in one week)",
    "7d/7": "cạo tất cả các ngày trong tuần (tapping without any day of tapping rest in a week)",
    "a chromosome": "nhiễm sắc thể",
    "a horizon": "Tầng A, tầng rửa trôi",
    "abandoned": "bỏ hóa, hưu canh",
    "abandoned land": "đất bỏ hóa, đất hưu canh",
    "aberrant": "sai lệch, biến dạng, khác thường",
    "aberration": "sự sai hình, sự biến dạng, sự lệch chuẩn",
    "ability": "khả năng, năng lực",
    "abiosis": "trạng thái sống ngầm, đời sống vô tinh"
}

@app.get("/lookup")
def lookup(term: str = Query(..., description="Từ tiếng Anh cần tra")):
    result = dictionary.get(term.strip().lower())
    if result:
        return {"term": term, "meaning": result}
    return JSONResponse(status_code=404, content={"error": "Không có trong từ điển"})
