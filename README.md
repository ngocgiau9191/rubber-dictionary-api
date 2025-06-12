# Rubber Dictionary Plugin

## Cách triển khai
1. Cài đặt yêu cầu:
   ```
   pip install fastapi uvicorn
   ```

2. Chạy server:
   ```
   uvicorn main:app --reload
   ```

3. Deploy lên Vercel/Render và cập nhật URL trong `ai-plugin.json` và `openapi.yaml`

4. Truy cập ChatGPT > Plugin > "Develop your own" và nhập URL tới file `.well-known/ai-plugin.json`
