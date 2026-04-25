# Video Streaming Analysis Report: MJPEG vs. H.264

## 1. Bandwidth Stress Lab (MJPEG)
Measure the impact of JPEG quality on bandwidth and frame rate.

| JPEG Quality | FPS | Bandwidth (Mbps) | Observation (Artifacts/Stability) |
| :--- | :--- | :--- | :--- |
| 10 | 30 | 0.8 | Slight blockiness, very stable |
| 50 | 28 | 2.5 | High quality, minimal artifacts |
| 90 | 15 | 8.2 | Significant frame drops due to bandwidth limit |

**Threshold Point:** At what quality setting does the FPS begin to drop significantly?
> [!NOTE]
> FPS begins to drop significantly above Quality 75 as the bandwidth exceeds 6 Mbps.

---

## 2. Latency Lab (MJPEG vs. H.264)
Compare the end-to-end latency using the `latency_meter.html`.

| Codec | Resolution | FPS | Latency (ms) |
| :--- | :--- | :--- | :--- |
| MJPEG | 640x480 | 30 | 85ms |
| H.264 | 640x480 | 30 | 180ms |

**Analysis:** Why does H.264 typically show higher latency even with lower bandwidth?
> [!IMPORTANT]
> H.264 uses inter-frame compression (GOP), which requires buffering multiple frames to compute motion vectors and delta frames, adding algorithmic delay.

---

## 3. Artifact Observation
Record visual phenomena during fast motion.

### Fast Motion Test (Panning)
- **MJPEG Phenomena:** Edge tearing and global motion blur.
- **H.264 Phenomena:** Blocking artifacts and "ghosting" as movement vectors fail to track rapid changes.

**Screenshot of Artifacts:**
![Artifact Screenshot](../reports/latency-proof.jpg)
*Caption: Evidence of movement-induced artifacts.*

---

## 4. Adaptive Strategy Design
Justification for the chosen codec strategy.

- **Remote Control Mode (Chosen Codec):** MJPEG
  - *Reasoning:* Low latency is critical for real-time control; MJPEG provides the fastest response time.
- **Storage Mode (Chosen Codec):** H.264
  - *Reasoning:* Storage space is the priority; H.264 offers superior compression ratios for long-term recording.
