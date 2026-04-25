# Video Streaming Analysis Report: MJPEG vs. H.264

## 1. Bandwidth Stress Lab (MJPEG)
Measure the impact of JPEG quality on bandwidth and frame rate.

| JPEG Quality | FPS | Bandwidth (Mbps) | Observation (Artifacts/Stability) |
| :--- | :--- | :--- | :--- |
| 10 | | | |
| 50 | | | |
| 90 | | | |

**Threshold Point:** At what quality setting does the FPS begin to drop significantly?
> [!NOTE]
> Record your answer here.

---

## 2. Latency Lab (MJPEG vs. H.264)
Compare the end-to-end latency using the `latency_meter.html`.

| Codec | Resolution | FPS | Latency (ms) |
| :--- | :--- | :--- | :--- |
| MJPEG | 640x480 | | |
| H.264 | 640x480 | | |

**Analysis:** Why does H.264 typically show higher latency even with lower bandwidth?
> [!IMPORTANT]
> Consider the impact of Group of Pictures (GOP) and buffer sizes.

---

## 3. Artifact Observation
Record visual phenomena during fast motion.

### Fast Motion Test (Panning)
- **MJPEG Phenomena:** (e.g., blur, tearing)
- **H.264 Phenomena:** (e.g., P-frame artifacts, blockiness)

**Screenshot of Artifacts:**
![Artifact Screenshot](../reports/latency-proof.jpg)
*Caption: Evidence of movement-induced artifacts.*

---

## 4. Adaptive Strategy Design
Justification for the chosen codec strategy.

- **Remote Control Mode (Chosen Codec):** [MJPEG / H.264]
  - *Reasoning:*
- **Storage Mode (Chosen Codec):** [MJPEG / H.264]
  - *Reasoning:*
