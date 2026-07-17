# Week 5 Visual Quick Reference Card

**🎯 One-Page Guide for Instructors**

---

## 📍 Critical Visuals by Segment

### Segment 2 (0:15-0:35) - Unsupervised vs Supervised
```
├─ supervised_vs_unsupervised.png (comparison table)
└─ customer_segmentation_example.png ⭐ CORE METAPHOR
   💡 Spend 8 min here - this sets up entire week!
```

### Segment 3 (0:35-1:10) - K-Means Deep Dive
```
├─ ANIMATION SEQUENCE ⭐⭐⭐ (10 minutes total)
│  ├─ frame1.png → Initial data
│  ├─ frame2.png → Initialize centroids
│  ├─ frame3.png → Assign points
│  ├─ frame4.png → Update centroids
│  └─ frame5.png → Convergence
│
├─ kmeans_bad_initialization.png (k-means++ motivation)
├─ kmeans_spherical_assumption.png (when K-Means fails)
└─ feature_scaling_impact.png ⭐ CRITICAL PATTERN
   💡 This prevents #1 student mistake!
```

### Segment 5 (1:25-1:55) - PCA Theory
```
├─ pca_intuition_3d_to_2d.png ⭐⭐⭐ MUG METAPHOR
│  💡 Spend 8 min - this is THE PCA intuition!
│
├─ pca_variance_explained.png
└─ pca_scree_plot.png
```

### Segment 6 & 7 - Live Coding
```
BACKUPS (if notebook fails):
├─ mall_customers_clusters.png
└─ mnist_2d_pca.png
```

### Day 2 - Deep Dive
```
├─ elbow_method.png
├─ silhouette_plot.png
└─ pca_variance_explained.png
```

---

## ⚡ Top 5 Teaching Moments

1. **Customer Segmentation** (Segment 2)
   - Visual: `customer_segmentation_example.png`
   - Time: 8 minutes
   - Why: Core metaphor for entire Week 5
   - Tip: Point to each cluster, assign business names

2. **K-Means Animation** (Segment 3)
   - Visual: 5 frames
   - Time: 10 minutes (2 min/frame)
   - Why: Algorithm clicks here!
   - Tip: Show frame → explain → show next frame

3. **Feature Scaling** (Segment 3)
   - Visual: `feature_scaling_impact.png`
   - Time: 7 minutes
   - Why: Prevents #1 student bug
   - Tip: Emphasize "ALWAYS scale!" at least 3 times

4. **PCA Mug Metaphor** (Segment 5)
   - Visual: `pca_intuition_3d_to_2d.png`
   - Time: 8 minutes
   - Why: Makes PCA intuitive, not just math
   - Tip: Ask "which view captures most detail?"

5. **K-Means Assumptions** (Segment 3)
   - Visual: `kmeans_spherical_assumption.png`
   - Time: 5 minutes
   - Why: Students need to know when it fails
   - Tip: Show left (works) then right (fails)

---

## 🚨 Common Pitfalls to Avoid

❌ **DON'T:** Rush K-Means animation frames (spend full 10 min)
❌ **DON'T:** Skip feature scaling visual (students will forget to scale)
❌ **DON'T:** Underestimate mug metaphor (PCA intuition lives here)
❌ **DON'T:** Show too many visuals at once (one at a time!)

✅ **DO:** Return to customer segmentation throughout session
✅ **DO:** Pause between animation frames for questions
✅ **DO:** Use laser pointer to highlight key parts of visuals
✅ **DO:** Ask students to interpret visuals before you explain

---

## 📏 Visual Display Checklist

**Before class:**
- [ ] Test all visuals on actual projector (colors may differ)
- [ ] Verify animation frames advance smoothly in slides
- [ ] Have backup plans for live coding segments
- [ ] Print customer segmentation visual (backup)

**During class:**
- [ ] Show visuals at full size (don't shrink)
- [ ] Use laser pointer for specific features
- [ ] Pause for questions after each major visual
- [ ] Return to key visuals when reviewing concepts

---

## 🎨 Visual Design Features

**All visuals include:**
- ✅ Bold titles (readable from back of room)
- ✅ Color-coded clusters (visually distinct)
- ✅ Annotations (key insights highlighted)
- ✅ Problem/Solution format (❌ vs ✅)
- ✅ 300 DPI (publication quality)

**Color system:**
- 🔴 Red boxes = Problem/Warning
- 🟢 Green boxes = Solution/Success
- 🟡 Yellow boxes = Information/Neutral

---

## 💾 File Locations

**All visuals:** `week5/instructor_materials/visuals/*.png`
**Generation script:** `generate_missing_visuals.py`
**Full guide:** `VISUAL_USAGE_GUIDE.md`
**Analysis:** `../../VISUALS_DISCONNECT_ANALYSIS.md`

---

## 🔧 Emergency Regeneration

If visual files are corrupted:
```bash
cd week5/instructor_materials/visuals
python generate_missing_visuals.py
```
Takes ~30 seconds, creates all 10 core teaching visuals.

---

## 📊 Visual Effectiveness Ratings

⭐⭐⭐ **CRITICAL** (don't skip):
- K-Means animation frames (1-5)
- Customer segmentation example
- PCA mug metaphor (3D-to-2D)
- Feature scaling impact

⭐⭐ **HIGH IMPACT**:
- K-Means spherical assumption
- k-means++ initialization
- Supervised vs unsupervised comparison

⭐ **SUPPORTING**:
- Elbow method (Day 2)
- Silhouette plot (Day 2)
- Scree plot (Segment 5)

---

## 🎯 Time Budget per Visual

**Animation frames:** 2 min each × 5 = 10 min total
**Customer segmentation:** 8 min (most important!)
**PCA mug metaphor:** 8 min (second most important!)
**Feature scaling:** 7 min (emphasize multiple times)
**Other visuals:** 3-5 min each

**Total visual time:** ~60 min out of 180 min session

---

## 💡 Pro Tips

1. **Show, don't tell:** Point to specific features in visuals
2. **Build anticipation:** "Let me show you something interesting..."
3. **Ask before explaining:** "What do you notice about this visual?"
4. **Connect visuals:** "Remember the customer segmentation from earlier?"
5. **Use animation frames like slides:** Advance through them smoothly

---

## 📱 Quick Visual Audit

Before teaching, verify you can answer YES to all:

**Segment 2:**
- [ ] Can show customer segmentation for 8 min?
- [ ] Can point to all 4 customer segments?

**Segment 3:**
- [ ] Can advance through 5 animation frames smoothly?
- [ ] Can show feature scaling side-by-side comparison?

**Segment 5:**
- [ ] Can explain mug metaphor for 8 min?
- [ ] Can interpret scree plot?

**Live coding:**
- [ ] Know where backup visuals are located?
- [ ] Tested notebook runs without errors?

---

**If all checks pass → Ready to teach! 🎓**

---

**Version:** 1.0
**Last updated:** 2026-03-09
**Print this card:** Keep at teaching station for quick reference
