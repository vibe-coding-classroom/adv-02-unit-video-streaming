#include <Arduino.h>

/**
 * @brief Configuration for MJPEG streaming
 * Focuses on intra-frame compression, suitable for low-latency but high bandwidth.
 */
void useMJPEG() {
    Serial.println("Switching to MJPEG mode...");
    // TODO: Implement MJPEG encoder initialization
    // 1. Stop current stream
    // 2. Set camera quality (e.g., 10-90)
    // 3. Start MJPEG server
}

/**
 * @brief Configuration for H.264 streaming
 * Focuses on inter-frame compression, high compression ratio but potential latency due to GOP and buffer.
 */
void useH264() {
    Serial.println("Switching to H.264 mode...");
    // TODO: Implement H.264 encoder initialization
    // 1. Stop current stream
    // 2. Configure bitrate and GOP size
    // 3. Start H.264 stream (RTSP/WebRTC)
}

void setup() {
    Serial.begin(115200);
    Serial.println("Video Streaming Unit Initialized");
    
    // Default to MJPEG for initial low-latency setup
    useMJPEG();
}

void loop() {
    // Implement state machine for REMOTE_CONTROL vs STORAGE_MODE
    // Check for serial commands or physical buttons to switch modes
}
