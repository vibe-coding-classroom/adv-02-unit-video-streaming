Viewed adv-02-unit-video-streaming.html:1-409

針對 **`adv-02-unit-video-streaming` (影像串流原理：MJPEG vs. H.264)** 單元，這是一個涉及「影像壓縮算法」與「端到端延遲 (Latency)」深度對應的課題。

以下是在 **GitHub Classroom** 部署其作業 (Assignments) 的具體建議：

### 1. 範本倉庫 (Template Repo) 配置建議
影像串流單元的範本應強調「量化測量工具」，建議包含：
*   **📂 `tools/latency_meter.html`**：一個顯示高速計數器的網頁。學員需將相機對準此螢幕，拍攝「原始螢幕」與「串流畫面」的並列照片，透過兩者數值差來計算 End-to-End 延遲。
*   **📂 `src/codec_manager.cpp`**：提供切換編解碼器的核心框架，預置 `useMJPEG()` 與 `useH264()` 介面。
*   **📂 `analysis/codec_bench.md`**：預置一個檢核清單，讓學員紀錄在不同動態場景（靜止 vs. 快速甩動）下的畫面崩潰現象（如馬賽克、果凍效應）。
*   **📂 `.github/workflows/artifact_audit.yml`**：設置檢查點，驗證學員是否有上傳延遲實測證明照片（如 `latency-proof.jpg`）。

---

### 2. 作業任務部署細節

#### 任務 1：頻寬殺手 MJPEG 壓力測試 (Bandwidth Stress Lab)
*   **目標**：理解「空間壓縮 (Intra-frame)」在物理層面的頻寬佔量。
*   **Classroom 部署建議**：
    *   **實驗要求**：學員需在 README 中紀錄 Quality 從 10 到 90 的過程中，$FPS$ 下降的臨界點。
    *   **數據提交**：提交一份測量表，對比在同一 Wi-Fi 底下，MJPEG 與 H.264 在相同畫質下的串流比特率 ($Mbps$)。這能讓學員深刻理解 H.264 十倍壓縮率的威力。

#### 任務 2：時空旅人 H.264 延遲觀測 (Latency & Artifacts Lab)
*   **目標**：量化解碼緩衝區與「時間預測 (Inter-frame)」帶來的代價。
*   **Classroom 部署建議**：
    *   **量化核核**：學員必須利用提供的 `latency_meter.html` 進行實測。
    *   **現象解釋**：在報告中描述為什麼快速甩動相機時，H.264 會出現「方塊殘影 (P-Frame Artifacts)」。導師應檢查學員是否能正確將此現象歸因於「運動向量預測失敗」。
    *   **提交證據**：上傳一張帶有明顯編碼殘影的截圖，並標註出這屬於哪一種類型的幀錯誤。

#### 任務 3：情境化編碼策略設計 (Adaptive Strategy Design)
*   **目標**：根據業務場景（即時遙控 vs. 錄影存證）設計動態切換策略。
*   **Classroom 部署建議**：
    *   **邏輯設計**：要求學員實作一個狀態機邏輯：
        - `State: REMOTE_CONTROL` -> 強制切換為 `MJPEG` (優先保證延遲低於 100ms)
        - `State: STORAGE_MODE` -> 切換為 `H.264` (優先保證節省 SD 卡空間)
    *   **驗證方式**：在 PR (Pull Request) 中審核其 `STRATEGY.md` 設計文檔。導師評估其是否考慮了切換編解碼器時，「系統重置時間」對控制連續性的影響。

---

### 3. 編碼導師點評標準 (Codec Benchmarks)
此單元的價值在於 **「對延遲成因的深度拆解」**：
*   [ ] **延遲識別力**：能否準確說出當前的 200ms 延遲中，是由於「網路擁塞」還是「H.264 緩衝過大」造成的？
*   [ ] **畫質解構力**：是否能透過觀察畫面，判斷出當前是否正在傳送 I-Frame (關鍵幀)？
*   [ ] **場景通透性**：在 README 中，學員是否能釐清：對於「視覺避障」功能的無人車，應該選擇哪種編碼方案並給出工程依據？

### 📁 推薦範本結構 (GitHub Classroom Template)：
```text
.
├── src/
│   └── codec_switcher.cpp  # 核心：學員實作動態切換邏輯
├── tools/
│   └── latency_meter.html  # 工具：用於量化端對端延遲
├── reports/
│   ├── latency-proof.jpg   # 證據：延遲測量截圖
│   └── artifact_test.md    # 分析：馬賽克、殘影現象紀錄報告
└── README.md               # 結語：我為遙控車選擇的最終編碼方案
```

透過這種部署方式，學生能從「會看影片」進化到「**理解每一幀數據背後的物理代價**」。這對於未來開發低延遲視訊系統（如 fpv、遠端手術、雲端串流遊戲）是絕對核心的基本功。_
