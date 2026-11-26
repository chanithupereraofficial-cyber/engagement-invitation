# Wedding Invitation Web Page (මංගල ඇරයුම)

An exact, complete, high-fidelity replica of the **Adeesha & Nethuli Wedding Invitation** web application with golden wedding rings artwork and custom music.

---

## ✨ Features Included

- **💌 Interactive Envelope Opening**: Realistic 3D flap unfold with gold monogram wax seal and sliding invitation card animation.
- **💍 Golden Wedding Rings Artwork**: The iconic interlocking gold wedding bands with sparkling diamond illustration, enlarged and enhanced with rich warm gold color saturation and seamless blend with the textured stationery.
- **🌐 Bilingual Support**: Full instant language switching between **Sinhala (සිංහල)** and **English (EN)** with specialized typography (Abhaya Libre, Pinyon Script, Maname, Sansala, and Great Vibes).
- **🌸 Animated Falling Petals**: Ambient floral blossom particle animation falling down the screen (with toggle option).
- **🎵 Romantic Background Music**: Embedded audio player with toggle mute/play button and your custom wedding track.
- **⏳ Real-time Countdown Timer**: Days, Hours, Minutes, and Seconds countdown to the special day.
- **📅 Event Programme & Venue**: Poruwa Ceremony, Lunch & Welcome schedule, Google Maps navigation link, and **Add to Calendar (.ics)** download.
- **📱 Responsive Mobile Dock**: Fixed floating bottom dock for smooth navigation between Home, Date, and Venue.

---

## 📁 Project Structure

```
wedding-invitation/
├── index.html        # Main self-contained wedding web page
├── README.md         # Documentation & guide
└── assets/           # High-resolution fonts, illustrations & audio
    ├── weddingRings.png        # Golden wedding rings illustration
    ├── wedding-song.mp3        # Custom background audio track
    ├── 254d773d80ecd382.ttf    # Abhaya font
    ├── 4aab130a6ed27f8b.ttf    # Pinyon Script font
    ├── db07b4953f547081.ttf    # Maname font
    ├── 2b0df6b8bde56d3b.ttf    # SerifSI font
    ├── 8d509802186f1b51.ttf    # Great Vibes font
    ├── 214cfdf7ddc5ea57.ttf    # Sansala font
    ├── feb0ebb1e7f145fd.jpg    # Premium paper background texture
    ├── bouquet.webp            # Floral bouquet art
    ├── outline.webp            # Floral outline art
    ├── venueArt.webp           # Venue architectural sketch
    ├── bouquet2.webp           # Corner floral art
    ├── spray.webp              # Decorative spray motif
    ├── ringsArt.webp           # Interlocking wedding rings illustration
    ├── countRose.webp          # Countdown rose graphic
    └── single.webp             # Single floral accent
```

---

## 🛠️ How to Customize Your Details

Open `index.html` in any text editor and edit the `WEDDING` configuration object starting at line 11:

```javascript
const WEDDING = {
  groom: { si: "අදීෂ", en: "Adeesha" },
  bride: { si: "නෙතුලි", en: "Nethuli" },
  parents: {
    groom: { si: ["අනුර විජේසිංහ", "දීපා විජේසිංහ"], en: ["Anura Wijesinghe", "Deepa Wijesinghe"] },
    bride: { si: ["සුනිල් සේනානායක", "මාලිනී සේනානායක"], en: ["Sunil Senanayake", "Malini Senanayake"] }
  },
  date: "2026-12-31",
  start: "09:30",
  end: "15:30",
  deadline: "2026-12-15",
  venue: { si: "සිනමන් ලේක්සයිඩ්", en: "Cinnamon Lakeside" },
  town: { si: "කොළඹ", en: "Colombo" },
  map: "https://www.google.com/maps/search/?api=1&query=Cinnamon+Lakeside+Colombo",
  groomPhone: "+94770000000",
  bridePhone: "+94770000001",
  whatsapp: "94770000000",
  rsvpEndpoint: "",
  schedule: [
    ["welcome", "09:30"],
    ["poruwa", "10:00"],
    ["lunch", "12:00"]
  ]
};
```

---

## 🚀 How to Run Locally

You can open `index.html` directly in your browser:
- Double click `index.html`, or right click and choose **Open with Google Chrome / Microsoft Edge / Safari**.

Alternatively, run a simple local web server:
```bash
# Using Python
python -m http.server 8080

# Using Node.js
npx serve .
```
Then visit `http://localhost:8080` in your web browser.

---

## 🌐 How to Deploy for Free (e.g., to Vercel)

1. Sign in to [Vercel](https://vercel.com).
2. Install Vercel CLI or push this folder to a GitHub repository.
3. Import the repository in Vercel and click **Deploy**! (No build configuration needed; it is static HTML/CSS/JS).
