# Architecture Evolution Module - Production Guide

**Module:** Neural Network Architecture Evolution (Week 7 Pre-Class)
**Duration:** 2 hours
**Format:** Recordable Video OR Live Lecture
**Purpose:** Complete workflow for recording and delivering this module

---

## Table of Contents

1. [Recording vs Live Teaching Decision](#recording-vs-live-teaching-decision)
2. [Recording Setup (Option A - Recommended)](#recording-setup-option-a---recommended)
3. [Live Teaching (Option B)](#live-teaching-option-b)
4. [Hybrid Approach (Recommended)](#hybrid-approach-recommended)
5. [Pre-Recording Preparation](#pre-recording-preparation)
6. [Recording Workflow](#recording-workflow)
7. [Editing Guide (Optional)](#editing-guide-optional)
8. [Hosting & Distribution](#hosting--distribution)
9. [Student Materials Distribution](#student-materials-distribution)
10. [Quality Checklist](#quality-checklist)
11. [Troubleshooting](#troubleshooting)

---

## Recording vs Live Teaching Decision

### Option A: Record Once, Reuse (Recommended)

**Advantages:**
- Students can pause, rewind, and rewatch difficult concepts
- Reusable across multiple cohorts (one-time effort)
- Can edit out mistakes and "umms"
- Students watch asynchronously (fits their schedule)
- Saves 2 hours of instructor time per cohort

**Disadvantages:**
- No real-time student questions
- Takes 3-4 hours total (2h recording + 1-2h editing/uploading)
- Requires basic recording equipment (microphone)
- Feels less personal

**Best For:**
- Cohorts with >10 students (reuse benefits multiply)
- Distributed/asynchronous learning
- Content that doesn't change often (architecture history is stable)

---

### Option B: Teach Live

**Advantages:**
- Real-time Q&A and interaction
- Can adapt to student confusion in the moment
- Builds instructor-student rapport
- No recording/editing time needed

**Disadvantages:**
- 2-hour commitment per cohort
- Students can't rewatch difficult parts
- No record for absent students
- Must re-teach for each cohort

**Best For:**
- Small cohorts (<10 students)
- Highly interactive learning cultures
- Content that changes frequently

---

### Hybrid Approach (Recommended)

**Workflow:**
1. **Pre-Week 7:** Students watch 2-hour recorded video asynchronously
2. **Week 7 Day 1 Start:** 15-20 minute live Q&A session
   - "What was confusing?"
   - "Let's revisit [difficult concept]"
   - Quick recap of decision framework

**Benefits:**
- Best of both worlds: reusable content + live interaction
- More hands-on time in Week 7 (don't spend 2h on lecture)
- Students come prepared with specific questions

**Recommendation:** Use this hybrid approach. Record once, reuse with live Q&A.

---

## Recording Setup (Option A - Recommended)

### Required Equipment

#### Microphone (CRITICAL - Good Audio > Good Video)

**Option 1: Blue Yeti USB Microphone ($100-150)**
- Professional podcasting quality
- USB plug-and-play (no audio interface needed)
- Gain control, mute button, headphone monitoring
- Recommended for long-term reuse

**Option 2: Blue Snowball USB Microphone ($50-70)**
- Good budget option
- USB plug-and-play
- Slightly lower quality than Yeti but very usable

**Option 3: Built-in Laptop Microphone (Free, NOT Recommended)**
- Use only if budget is $0
- Test extensively - often picks up keyboard noise, fan noise
- Students will struggle with poor audio

**Critical:** If you can only invest in ONE thing, invest in a microphone. Students will forgive mediocre visuals but not inaudible audio.

#### Recording Software

**Option 1: OBS Studio (Free, Recommended)**
- Professional open-source recording software
- Records screen + webcam (optional)
- Supports multiple scenes
- Learning curve: 30-60 min tutorial
- Download: https://obsproject.com/

**Option 2: Zoom (Free with time limit, Easy)**
- Record local meeting with screen share
- Familiar if you already use Zoom for teaching
- 40-minute limit on free tier (record 3 segments separately)
- Paid Zoom Pro ($150/year): unlimited time

**Option 3: Loom ($8/month or Free tier)**
- Browser-based screen recording
- Very easy to use (5 min learning curve)
- Free tier: 5 min videos (must record many segments)
- Paid tier: unlimited length
- Good for quick recordings

**Recommendation:** OBS Studio (one-time 1h learning investment, free forever, professional quality)

#### Optional Equipment

**Webcam (Optional):**
- Built-in laptop webcam is fine
- Students care more about seeing diagrams than seeing your face
- Consider picture-in-picture (small webcam corner) or no webcam at all

**Lighting (Optional but helps):**
- Record in well-lit room
- Face a window (natural light) or use desk lamp
- Avoid backlighting (window behind you)

**Headphones (Recommended):**
- Monitor your audio while recording
- Catch issues (breathing too close to mic, fan noise) in real-time

---

### Recording Space Setup

**Environment:**
- **Quiet room:** Close door, turn off fans/AC if possible
- **Minimal echo:** Soft furnishings help (curtains, carpet, bookshelves absorb sound)
- **Stable internet:** Only needed if uploading large files; recording is offline

**Computer Prep:**
- **Close notifications:** Turn on Do Not Disturb mode
- **Close unnecessary apps:** Browser tabs, Slack, email
- **Disable desktop notifications:** Calendar, messaging apps
- **Full battery or plugged in:** 2-hour recording drains battery

**Microphone Position:**
- 6-8 inches from mouth (one hand width)
- Slightly off-axis (not breathing directly into it)
- Pop filter helps (or improvise with pencil + sock)

---

## Pre-Recording Preparation

### 1. Create All Visual Materials (Session 3)

**Required Visuals (14 diagrams from VISUAL_SPECIFICATIONS.md):**
- Visual 1: Perceptron diagram
- Visual 2: Multi-Layer Perceptron
- Visual 3: XOR decision boundary
- Visual 4: Dense vs Conv parameter comparison
- Visual 5: Convolutional filter animation
- Visual 6: Feature hierarchy (cat image)
- Visual 7: Gradient flow comparison
- Visual 8: Residual block diagram
- Visual 9: RNN unrolled through time
- Visual 10: LSTM cell simplified
- Visual 11: Attention matrix heatmap
- Visual 12: RNN vs Transformer processing
- Visual 13: Historical timeline poster
- Visual 14: Architecture selection flowchart

**Creation Tools:**
- **Diagrams:** Draw.io (free), PowerPoint, Excalidraw
- **Timeline/Infographics:** Canva (has templates)
- **Plots/Heatmaps:** Python (matplotlib, seaborn)
- **Animations:** PowerPoint animations (export as video) OR Matplotlib FuncAnimation

**Assembly:**
- Create slide deck (PowerPoint, Google Slides, Keynote)
- One visual per slide (or grouped logically)
- Minimal text (diagrams should speak for themselves)
- Large fonts (24pt minimum - visible in recordings)

**Time Estimate:** 3-4 hours to create all 14 visuals

---

### 2. Prepare Speaker Notes (Session 4)

**Using TEACHING_SCRIPT.md:**
- Copy verbatim scripts into slide deck speaker notes
- Mark timing cues (e.g., "0:05 - Transition to Segment 1")
- Highlight key analogies in bold
- Note where to pause for emphasis

**Practice Run (Recommended):**
- Do one dry run through entire 2 hours
- Time each segment (they may run long first time)
- Identify tongue-twisters or awkward phrasing
- Revise scripts based on what feels natural

**Time Estimate:** 2-3 hours (1h script prep + 1-2h practice run)

---

### 3. Test Recording (CRITICAL)

**5-Minute Test Recording:**
1. Set up microphone, recording software
2. Record 5 minutes of teaching (pick any segment)
3. Play back recording:
   - **Audio clear?** (No background noise, fan hum, breathing?)
   - **Visuals sharp?** (Text readable, diagrams clear?)
   - **Pace good?** (Not too fast or slow?)
4. Adjust microphone position, gain, screen resolution
5. Re-record test until satisfied

**Common Issues:**
- **Audio too quiet:** Increase microphone gain, move closer
- **Audio too loud/distorted:** Decrease gain, move farther away
- **Background noise:** Close windows, turn off AC, use noise gate in OBS
- **Screen blurry:** Record at 1080p (1920×1080) minimum

**Time Estimate:** 30 minutes

---

## Recording Workflow

### Option 1: Record in Segments (Recommended)

**Why Segments?**
- Easier to re-record if you make a mistake (just redo one segment)
- Natural break points (matches attention span structure)
- Can record on different days if needed

**Segment Structure (7 files):**
- `Segment0_Intro.mp4` (5 min)
- `Segment1_DenseNetworks.mp4` (20 min)
- `Segment2_CNNs.mp4` (20 min)
- `BREAK_SLIDE.mp4` (5 min - optional, or insert in editing)
- `Segment3_ResNet.mp4` (20 min)
- `Segment4_RNN_LSTM.mp4` (20 min)
- `Segment5_Transformers.mp4` (20 min)
- `Segment6_DecisionFramework.mp4` (10 min)

**Recording Each Segment:**
1. **Start recording**
2. **Silence (3-5 seconds):** Makes editing easier (trim clean start)
3. **Teach segment** following speaker notes
4. **If mistake:**
   - Pause 3 seconds (creates silence gap for editing)
   - Restart sentence from natural break point
   - Continue (don't stop recording)
5. **End silence (3-5 seconds):** Makes editing easier (trim clean end)
6. **Stop recording**
7. **Save file** with descriptive name

**Time Estimate:** 2.5-3 hours (2h content + 0.5-1h mistakes/restarts)

---

### Option 2: Record Continuously (Not Recommended)

**Workflow:**
1. Hit record
2. Teach entire 2 hours straight through
3. Stop recording

**Pros:** One file, no editing needed
**Cons:** Any mistake requires re-recording entire 2 hours OR complex editing

**Recommendation:** Only do this if you're very experienced with live teaching and rarely make mistakes.

---

### During Recording - Pro Tips

**Pacing:**
- Slightly slower than normal conversation (students are listening, not responding)
- Pause 2-3 seconds after key concepts (gives time to process)
- Pause before transitions (signals new topic)

**Energy:**
- Stand up while recording (more energetic voice)
- Smile while talking (comes through in audio - sounds warmer)
- Imagine teaching one student (not a camera)

**Hydration:**
- Water nearby (vocal cords dry out)
- Take sip during slide transitions (mute or edit out)

**Mistakes:**
- Don't say "oops" or "let me redo that" (just pause and restart)
- Small mistakes (minor stumbles) are fine - students relate to authenticity
- Only redo if you misstated a fact or got completely tangled

---

## Editing Guide (Optional)

### Minimal Editing (Recommended)

**Tools:** iMovie (Mac, free), Windows Video Editor (Windows, free), DaVinci Resolve (advanced, free)

**Basic Workflow (30-60 minutes):**
1. **Import all segment files** into editor
2. **Trim start/end** (remove silence buffers)
3. **Add title card** at beginning:
   - "Neural Network Architecture Evolution"
   - "Week 7 Pre-Class Module"
   - "Duration: 2 hours"
4. **Add break slide** at 45-minute mark:
   - "5-Minute Break"
   - "Stretch, grab water, back at [timestamp]"
5. **Add segment divider slides** (optional):
   - "Milestone 1: Dense Networks"
   - "Milestone 2: Convolutional Networks"
   - etc.
6. **Export as MP4** (H.264 codec, 1080p, 30fps)

**Time Estimate:** 30-60 minutes

---

### Advanced Editing (Optional)

**Additional touches (adds 1-2 hours):**
- Remove mistakes (cut out pauses where you restarted)
- Add background music (very subtle, 10% volume during intro/break)
- Add on-screen text highlights (key terms appear as you say them)
- Add visual transitions between segments (fade, slide)
- Add lower-third graphics (your name, module title)

**Recommendation:** Skip advanced editing. Students prefer authentic teaching over polished production. Your time is better spent on content quality.

---

### Editing Checklist

- [ ] All segments trimmed (no dead silence)
- [ ] Title card at start (module name, your name, duration)
- [ ] Break slide at 45-minute mark
- [ ] Audio levels consistent across segments
- [ ] Video transitions smooth (not jarring cuts)
- [ ] Exported at 1080p (1920×1080) minimum
- [ ] File size reasonable (<2GB for 2 hours - aim for ~800MB-1.5GB)

---

## Hosting & Distribution

### Option 1: YouTube Unlisted + LMS Embed (Recommended)

**Workflow:**
1. **Upload to YouTube:**
   - Create YouTube account (free)
   - Click "Create" → "Upload video"
   - Select final edited MP4 file
   - **Privacy:** Unlisted (not Public - students need link to access)
   - **Title:** "Neural Network Architecture Evolution - Week 7 Pre-Class"
   - **Description:** Include learning objectives, timestamps
   - **Thumbnail:** Use title card screenshot
   - Processing takes 10-30 minutes for 2-hour video

2. **Embed in LMS (Canvas, Blackboard, Moodle):**
   - Copy YouTube URL
   - In LMS, create "Week 7 Pre-Class" module
   - Add "External Tool" or "Media" item
   - Paste YouTube URL
   - LMS will embed video player

**Advantages:**
- Unlimited storage (YouTube is free)
- Reliable streaming (YouTube CDN)
- Students don't need YouTube account to watch unlisted
- Can add chapter markers in YouTube (clickable timestamps)
- LMS tracks completion (if configured)

**Disadvantages:**
- Requires YouTube account
- Unlisted videos can be shared (anyone with link can watch)
- YouTube Terms of Service apply

---

### Option 2: Vimeo (Alternative)

**Workflow:**
1. Create Vimeo account
2. Upload video (free tier: 500MB/week limit - need Vimeo Plus $7/month for 2h video)
3. Set privacy to "Hide from Vimeo"
4. Embed in LMS

**Advantages:**
- More professional look (no ads, cleaner player)
- Better privacy controls (password protection, domain whitelisting)
- Higher quality streaming codec

**Disadvantages:**
- Free tier insufficient (must pay $7-20/month)
- Slower upload than YouTube

---

### Option 3: LMS Direct Upload

**Workflow:**
1. Export video as MP4
2. Upload directly to LMS media library
3. Embed in course module

**Advantages:**
- All content in one place
- Maximum privacy (only enrolled students)

**Disadvantages:**
- File size limits (many LMS cap at 500MB-1GB)
- Slower streaming (LMS servers slower than YouTube)
- Uses LMS storage quota

**Recommendation:** Only use if institutional policy prohibits external hosting.

---

### Option 4: Google Drive + Link Share

**Workflow:**
1. Upload MP4 to Google Drive
2. Right-click → "Get link" → "Anyone with link can view"
3. Share link with students

**Advantages:**
- Free, unlimited storage (if you have institutional Google Workspace)
- Easy to update video (replace file, link stays same)

**Disadvantages:**
- Streaming can be slow for large files
- Students must download or use Google Drive video player (clunky)
- Link can be shared widely

**Recommendation:** Use only as backup hosting or if YouTube/Vimeo unavailable.

---

### Video Metadata for Distribution

**Timestamps to include in description:**
```
0:00 - Introduction & Motivation
0:05 - Milestone 1: Dense Networks (Perceptron, XOR, MLP, Backpropagation, ReLU)
0:25 - Milestone 2: CNNs (Parameter Explosion, Convolution, Feature Hierarchy)
0:45 - BREAK (5 minutes)
0:50 - Milestone 3: ResNet (Degradation Problem, Skip Connections, Gradient Flow)
1:10 - Milestone 4: RNN/LSTM (Sequences, Vanishing Gradients, Gates)
1:30 - Milestone 5: Transformers (Attention, Parallelization, Multi-Head)
1:50 - Decision Framework & Wrap-Up
```

**Learning Objectives to include:**
- Map problem types to architecture families
- Understand why architectures evolved (problem-driven history)
- Apply heuristics for layer counts, neuron counts, activation functions
- Use decision framework for Week 7-8 projects

---

## Student Materials Distribution

### Files to Provide

**In LMS "Week 7 Pre-Class" Module:**

1. **Video Link** (embedded or direct link)

2. **Architecture_Evolution_Study_Guide.pdf** (8-12 pages)
   - Download link in LMS
   - OR print handouts for in-person students

3. **Architecture_Decision_Framework.pdf** (1 page)
   - Quick reference sheet
   - Students can print or keep open during Week 7 projects

4. **Further_Reading.md** (optional deep dive)
   - For interested students
   - Not required but enhances learning

5. **Architecture_Timeline_Poster.pdf** (optional)
   - Visual timeline 1958-2024
   - Can print as poster for classroom

---

### Student Instructions

**Announcement Template:**

```
Subject: Week 7 Pre-Class: Neural Network Architecture Evolution (Due [DATE])

Hi everyone,

Before we dive into Week 7's hands-on neural network projects, please watch
this 2-hour pre-class module on neural network architecture evolution.

**What You'll Learn:**
- WHY neural networks are designed the way they are
- The historical problems that led to CNNs, ResNet, LSTMs, and Transformers
- How to choose the right architecture for your project

**Materials:**
1. Video (2 hours): [LINK]
   - Includes 5-minute break at 45-minute mark
   - Feel free to pause and rewatch sections

2. Study Guide: [DOWNLOAD LINK]
   - Review this before Week 7 Day 1

3. Decision Framework (1-page reference): [DOWNLOAD LINK]
   - Keep this handy for Week 7 projects

**Due:** [DATE] before Week 7 Day 1
We'll have a 15-minute Q&A at the start of Week 7 to clarify anything confusing.

**Timestamps (for easy navigation):**
- 0:00 - Introduction
- 0:05 - Dense Networks (Perceptron → MLP → ReLU)
- 0:25 - CNNs (Parameter Explosion → Convolution)
- 0:45 - BREAK
- 0:50 - ResNet (Depth Problem → Skip Connections)
- 1:10 - RNN/LSTM (Sequences → Gates)
- 1:30 - Transformers (Attention Mechanism)
- 1:50 - Decision Framework

See you in Week 7!
[YOUR NAME]
```

---

## Quality Checklist

### Pre-Recording

- [ ] All 14 visuals created and in slide deck
- [ ] Speaker notes prepared from TEACHING_SCRIPT.md
- [ ] 5-minute test recording completed and reviewed
- [ ] Microphone positioned correctly (6-8 inches, off-axis)
- [ ] Recording software configured (1080p, correct mic selected)
- [ ] Environment quiet (door closed, notifications off)
- [ ] Water nearby, comfortable setup

### During Recording

- [ ] 3-5 second silence buffer at start of each segment
- [ ] Speaking pace slightly slower than normal conversation
- [ ] Pausing 2-3 seconds after key concepts
- [ ] Mistakes handled with pause + restart (no "oops")
- [ ] Energy consistent (standing, smiling, hydrated)
- [ ] 3-5 second silence buffer at end of each segment

### Post-Recording

- [ ] All segment files saved with descriptive names
- [ ] Audio clear (no background noise, distortion)
- [ ] Visuals sharp (text readable at 1080p)
- [ ] Timing approximately matches plan (±5 min per segment acceptable)

### Editing

- [ ] Start/end silence trimmed
- [ ] Title card added
- [ ] Break slide inserted at 45-minute mark
- [ ] Audio levels consistent across segments
- [ ] Exported as MP4, H.264, 1080p, 30fps
- [ ] File size <2GB (compression if needed)

### Distribution

- [ ] Video uploaded to hosting platform (YouTube/Vimeo/LMS)
- [ ] Privacy settings correct (unlisted/private)
- [ ] Timestamps added to description
- [ ] Study Guide PDF uploaded to LMS
- [ ] Decision Framework PDF uploaded to LMS
- [ ] Further Reading uploaded to LMS
- [ ] Student announcement sent with all links

### Week 7 Integration

- [ ] Video due date set (2-3 days before Week 7 Day 1)
- [ ] 15-minute Q&A scheduled at start of Week 7 Day 1
- [ ] Reminder sent 1 day before due date
- [ ] Completion tracking configured in LMS (if possible)

---

## Troubleshooting

### Recording Issues

**Problem: Audio has echo/reverb**
**Solution:** Record in smaller room with soft furnishings, or hang blankets on walls

**Problem: Background noise (traffic, HVAC, neighbors)**
**Solution:** Record late at night/early morning, use noise gate in OBS, or use Krisp.ai (noise cancellation software)

**Problem: Microphone sounds muffled**
**Solution:** Check mic isn't covered, increase gain, position closer to mouth

**Problem: Recording lags/drops frames**
**Solution:** Close all other apps, record to fast SSD (not external USB drive), lower recording quality to 720p

**Problem: Can't see cursor/mouse in recording**
**Solution:** Enable "Capture Cursor" in OBS, or use larger cursor in OS settings

---

### Distribution Issues

**Problem: YouTube upload stuck at processing**
**Solution:** Upload during off-peak hours (late night US time), or try Vimeo

**Problem: File too large for LMS (>1GB)**
**Solution:** Re-export with higher compression (lower bitrate), or use external hosting

**Problem: Students can't access YouTube (firewall)**
**Solution:** Mirror to Vimeo or LMS direct upload

**Problem: Video buffers/stutters for students**
**Solution:** Upload to YouTube (better CDN), or provide download link for offline viewing

---

### Content Issues

**Problem: Segment ran too long (30 min instead of 20 min)**
**Solution:** Acceptable! Better to teach thoroughly than rush. Adjust break timing.

**Problem: Forgot to mention key concept during recording**
**Solution:** Record 2-minute "supplement" video, post separately OR mention in Week 7 Day 1 Q&A

**Problem: Misstated a fact during recording**
**Solution:** Re-record segment OR post correction in LMS announcement OR address in Week 7 Q&A

**Problem: Student feedback says "too fast" or "too slow"**
**Solution:** YouTube playback speed (0.75×, 1.25×, 1.5×) solves this! Mention in announcement.

---

## Time Investment Summary

**One-Time Setup (First Cohort):**
- Create 14 visuals: 3-4 hours
- Prepare speaker notes: 1 hour
- Practice run: 1-2 hours
- Test recording: 30 minutes
- **Total Setup: 5.5-7.5 hours**

**Recording (Per Cohort if Live, One-Time if Recorded):**
- Recording segments: 2.5-3 hours
- **Total Recording: 2.5-3 hours**

**Post-Production (One-Time if Recorded):**
- Basic editing: 30-60 minutes
- Upload & configure: 30 minutes
- Create student announcement: 15 minutes
- **Total Post-Production: 1.25-1.75 hours**

**Grand Total (Record Once Approach): 9-12 hours one-time investment**

**Time Saved Per Cohort After First Recording:**
- Live teaching would take 2 hours per cohort
- Recorded module takes 15 minutes (Week 7 Q&A) per cohort
- **Savings: 1.75 hours per cohort**
- **Break-even after 6 cohorts** (12 hours / 1.75 hours)

---

## Recommended Timeline

**3-4 Weeks Before Week 7:**
- Create all 14 visuals (Session 3): 3-4 hours
- Prepare speaker notes (Session 4): 1 hour
- Practice dry run: 1-2 hours

**2 Weeks Before Week 7:**
- Test recording setup: 30 minutes
- Record all segments: 2.5-3 hours (can split across 2-3 days)

**1 Week Before Week 7:**
- Edit video: 30-60 minutes
- Upload to hosting: 30 minutes
- Create student materials: 1-2 hours (Session 5)
- Upload all PDFs to LMS: 15 minutes

**5-7 Days Before Week 7 Day 1:**
- Send student announcement with video link
- Set due date: 2-3 days before Week 7 Day 1

**Week 7 Day 1:**
- 15-minute Q&A at start of session
- Proceed with hands-on Keras (more time available!)

---

## Success Metrics

**Module succeeds when:**

- [ ] **>80% of students** watch video before Week 7 Day 1
- [ ] **Students can answer** during Q&A:
  - "When would you use a CNN vs a Transformer?"
  - "Why does ResNet use skip connections?"
  - "What problem does attention solve?"
- [ ] **Fewer architecture confusion questions** during Week 7 hands-on
- [ ] **Students apply decision framework** in Week 7-8 projects
- [ ] **Video quality acceptable:**
  - Audio clear and intelligible
  - Visuals readable
  - Pacing appropriate (not too fast/slow)
- [ ] **Instructor satisfied** with content accuracy and completeness

---

## Conclusion

This production guide provides a complete workflow for recording and delivering the Architecture Evolution module. The **recommended approach** is:

1. **Record once** using segmented recording (7 segments)
2. **Minimal editing** (trim + title card + break slide)
3. **Host on YouTube Unlisted** + embed in LMS
4. **Provide Study Guide + Decision Framework** as downloadable PDFs
5. **Hold 15-minute live Q&A** at start of Week 7

This approach balances quality, reusability, and time investment. After the initial 9-12 hour creation, you'll save 1.75 hours per cohort compared to live teaching—breaking even after 6 cohorts.

**Good luck with your recording!** Remember: students care most about clear audio and solid content. Don't over-polish. Authentic teaching beats Hollywood production.
