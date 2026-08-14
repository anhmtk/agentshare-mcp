# Upload this dataset to Hugging Face (manual)

Dataset đã tồn tại: https://huggingface.co/datasets/anhmtk/agentshare-multi-chain-defi

**Không** tạo dataset mới. **Không** đẩy lên repo `agentshare-openclaw`.

Bốn file `*.sample.json` **không cần upload lại** (schema không đổi). Lần này chỉ cần **thay `README.md`** để Hub tách 4 file thành 4 subset — hết lỗi `StreamingRowsError` / `CastError`.

## Re-upload README (fix Dataset Viewer)

1. Mở https://huggingface.co/datasets/anhmtk/agentshare-multi-chain-defi
2. Tab **Files and versions**
3. Nút **Add file** → **Upload file**
4. Kéo thả **đúng file local này** (không copy-paste nội dung):

   `D:\agentshare-mcp\integrations\huggingface\dataset\README.md`

   **Sai file thường gặp:** `D:\agentshare-mcp\integrations\huggingface\README.md`  
   (đó là card **Space/Gradio**, ~1394 bytes, YAML `sdk: gradio` — **không** có `configs`, viewer vẫn CastError).

   File đúng ~3199 bytes, dòng đầu sau `---` phải là `license: mit`, phải có block `configs:`.

5. Hugging Face sẽ hỏi overwrite `README.md` vì tên trùng — chọn overwrite / replace.
6. Commit message gợi ý:

   `Split sample JSON into per-endpoint configs to fix Dataset Viewer CastError`

7. **Commit changes to `main`**

8. **Verify ngay trên Hub** (trước khi đợi viewer): Files and versions → `README.md` → dòng đầu phải là:

   ```
   ---
   license: mit
   ```

   và phải thấy `configs:` với 4 `config_name`. Nếu thấy `title: AgentShare Solana DeFi` / `sdk: gradio` thì đang upload nhầm file Space — làm lại bước 4.

### Cấm làm khi upload card

- **Đừng** dùng nút **Edit dataset card** (rich editor) rồi dán markdown — UI hay **cắt mất** block YAML giữa hai dòng `---`.
- File **phải** bắt đầu bằng `---` rồi `license: mit` rồi block `configs:` (4 subset). Nếu thiếu `configs`, viewer lại gộp 4 JSON → CastError cũ.

## Chờ viewer rebuild

Sau commit, Hub chạy lại job Dataset Viewer (thường **1–5 phút**, đôi khi ~10 phút).

1. Reload trang dataset (Ctrl+F5).
2. Ở **Dataset Viewer**, dropdown **Subset** phải có 4 mục:
   - `meteora_brief` (default)
   - `dex_overview`
   - `service_meta`
   - `solana_dex_brief`
3. Chọn từng subset — mỗi cái hiện **1 row**, không còn `CastError`.

Nếu vẫn thấy lỗi cũ: đợi thêm vài phút rồi hard-refresh. Job cũ có thể còn cache.

## First-time create (chỉ khi dataset chưa có)

1. Open https://huggingface.co/new-dataset
2. Owner: `anhmtk`
3. Dataset name: **`agentshare-multi-chain-defi`** (khớp Space)
4. License: MIT · Public
5. Upload **cả** `README.md` **và** 4 file `*.sample.json` từ thư mục này (drag & drop). Giữ nguyên YAML đầu `README.md`.

## Fix “YAML Metadata Warning”

Warning này **không làm hỏng dataset** — chỉ mất badge license/tags trên Hub. Nguyên nhân thường gặp: README trên HF **không còn** frontmatter YAML.

**Cách sửa:** Files and versions → Upload lại `README.md` từ repo này (phải bắt đầu bằng `---` + `license: mit` + `configs:`). Refresh Dataset card.

## After publish

Dataset URL:

`https://huggingface.co/datasets/anhmtk/agentshare-multi-chain-defi`

Trong README Space (nếu muốn) thêm dòng link dataset đó.
