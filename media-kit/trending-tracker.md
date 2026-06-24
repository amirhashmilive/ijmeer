# Trending Topic Tracker — Logic & Calendar

> **Purpose:** Documents the trending detection logic and important dates calendar
> for automated post generation via GitHub Actions.

---

## 1. Trending Detection Logic

### Overview
A GitHub Actions workflow runs daily at 08:00 UTC to detect trending academic topics
and generate timely social media posts. The system uses the Gemini API to generate
contextually relevant content based on:

1. **Calendar events** — Known academic dates, festivals, scholar anniversaries
2. **Seasonal relevance** — Submission deadlines, conference seasons
3. **Historical context** — Birth/death anniversaries of notable scholars

### Trigger Criteria
A trending post is generated when ANY of these conditions are met:

| Condition | Example |
|-----------|---------|
| Today matches a calendar event (±1 day) | World Science Day (Nov 10) |
| Today is a scholar's birth/death anniversary (±1 day) | Ibn Sina's birthday |
| A major academic award is announced | Nobel Prize season (October) |
| Significant global academic event occurs | UNESCO declarations |

### Workflow
```
Daily Cron (08:00 UTC)
  ↓
Check today's date against calendar (Section 3)
  ↓
If match found → Generate trending post via Gemini API
  ↓
Generate platform-specific images via image API
  ↓
Save to media-kit/trending/YYYY-MM-DD-topic-slug.md
  ↓
Commit & push to main branch
```

---

## 2. Post Generation Format

Each trending post file (`YYYY-MM-DD-topic-slug.md`) contains:

```markdown
---
date: YYYY-MM-DD
topic: "Topic Title"
category: scholar|event|festival|breaking
platforms: linkedin,twitter,instagram,facebook,whatsapp
---

## LinkedIn Post
[content]

## Twitter Post 1
[content]

## Twitter Post 2
[content]

## Instagram Post
[content]

## Facebook Post
[content]

## WhatsApp Post
[content]
```

---

## 3. Important Dates Calendar

### Prominent Scholars & Scientists — Birth/Death Anniversaries

#### Islamic Golden Age Scholars

| Scholar | Field | Born | Died | Key Contribution |
|---------|-------|------|------|-----------------|
| **Al-Khwarizmi** | Mathematics, Astronomy | c. 780 | c. 850 | Father of Algebra |
| **Ibn Sina (Avicenna)** | Medicine, Philosophy | Aug 980 | Jun 1037 | Canon of Medicine |
| **Al-Biruni** | Astronomy, Physics | Sep 4, 973 | Dec 13, 1048 | Polymath, geodesy |
| **Ibn al-Haytham** | Optics, Scientific Method | Jul 1, 965 | Mar 6, 1040 | Father of Optics |
| **Al-Razi (Rhazes)** | Medicine, Chemistry | Aug 26, 854 | Oct 925 | Smallpox/measles distinction |
| **Omar Khayyam** | Mathematics, Poetry | May 18, 1048 | Dec 4, 1131 | Cubic equations, Rubaiyat |
| **Nasir al-Din al-Tusi** | Astronomy, Mathematics | Feb 18, 1201 | Jun 26, 1274 | Tusi couple, trigonometry |
| **Ibn Khaldun** | Sociology, Historiography | May 27, 1332 | Mar 17, 1406 | Muqaddimah, social science |
| **Jabir ibn Hayyan** | Chemistry | c. 721 | c. 815 | Father of Chemistry |
| **Al-Jazari** | Engineering | 1136 | 1206 | Mechanical engineering |
| **Ibn Rushd (Averroes)** | Philosophy, Medicine | Apr 14, 1126 | Dec 10, 1198 | Aristotelian philosophy |
| **Al-Idrisi** | Geography, Cartography | 1100 | 1165 | Tabula Rogeriana |

#### Modern Scientists

| Scientist | Field | Born | Died | Key Contribution |
|-----------|-------|------|------|-----------------|
| **Albert Einstein** | Physics | Mar 14, 1879 | Apr 18, 1955 | Theory of Relativity |
| **Marie Curie** | Physics, Chemistry | Nov 7, 1867 | Jul 4, 1934 | Radioactivity research |
| **Isaac Newton** | Physics, Mathematics | Jan 4, 1643 | Mar 31, 1727 | Laws of motion, calculus |
| **Galileo Galilei** | Astronomy, Physics | Feb 15, 1564 | Jan 8, 1642 | Heliocentrism, telescopic astronomy |
| **Charles Darwin** | Biology | Feb 12, 1809 | Apr 19, 1882 | Theory of Evolution |
| **Stephen Hawking** | Theoretical Physics | Jan 8, 1942 | Mar 14, 2018 | Black hole radiation |
| **Nikola Tesla** | Electrical Engineering | Jul 10, 1856 | Jan 7, 1943 | AC electricity |
| **C.V. Raman** | Physics | Nov 7, 1888 | Nov 21, 1970 | Raman Effect |
| **APJ Abdul Kalam** | Aerospace, Leadership | Oct 15, 1931 | Jul 27, 2015 | Missile Man of India |
| **Srinivasa Ramanujan** | Mathematics | Dec 22, 1887 | Apr 26, 1920 | Number theory |
| **Homi J. Bhabha** | Nuclear Physics | Oct 30, 1909 | Jan 24, 1966 | Indian nuclear program |

### Academic Festivals & International Days

| Date | Event | Category |
|------|-------|----------|
| **Jan 24** | International Day of Education | education |
| **Feb 11** | International Day of Women and Girls in Science | science |
| **Feb 13** | World Radio Day | media |
| **Feb 28** | National Science Day (India — Raman Effect) | science |
| **Mar 14** | Pi Day / Einstein's Birthday | science |
| **Mar 21** | World Poetry Day | humanities |
| **Apr 23** | World Book and Copyright Day | publishing |
| **Apr 26** | World Intellectual Property Day | legal |
| **May 3** | World Press Freedom Day | media |
| **Jun 5** | World Environment Day | science |
| **Jul 11** | World Population Day | social science |
| **Jul 15** | World Youth Skills Day | education |
| **Aug 12** | International Youth Day | education |
| **Sep 8** | International Literacy Day | education |
| **Sep 21** | International Day of Peace | social science |
| **Sep 28** | International Day for Universal Access to Information | publishing |
| **Oct 1** | International Day of Older Persons | social science |
| **Oct 5** | World Teachers' Day | education |
| **Oct (varies)** | Nobel Prize Announcements | science |
| **Nov 10** | World Science Day for Peace and Development | science |
| **Nov 14** | Children's Day (India) | education |
| **Nov (3rd Thu)** | World Philosophy Day | humanities |
| **Dec 10** | Human Rights Day | legal |
| **Dec 10** | Nobel Prize Ceremony | science |

### Indian Academic Calendar Events

| Period | Event |
|--------|-------|
| **Apr–Jun** | IJMEER Vol. X, Issue 1 publication window |
| **Jul–Sep** | Call for Papers — October issue |
| **Oct–Dec** | IJMEER Vol. X, Issue 2 publication window |
| **Jan–Mar** | Call for Papers — April issue |

---

## 4. Post Categories & Templates

### Scholar/Scientist Tribute
```
🌟 Remembering [Name] ([Birth Year]–[Death Year])

On this day, we honor [Name], the [nationality] [field] whose groundbreaking work
on [contribution] changed the world.

[2-3 sentences about their key contribution]

At IJMEER, we continue the tradition of advancing multidisciplinary knowledge.

🌐 www.ijmeer.com
#IJMEER #[Field] #[Name] #AcademicHeritage #OpenAccess
```

### Academic Event/Day
```
📅 [Event Name] — [Date]

Today we celebrate [event purpose]. [1-2 sentences about significance]

IJMEER is committed to [relevant connection to the event].

Submit your research: www.ijmeer.com/call-for-papers.html

#IJMEER #[EventHashtag] #OpenAccess #AcademicResearch
```

### Festival/Cultural
```
🎉 [Festival Name] Greetings from IJMEER!

Wishing our global academic community a [adjective] [festival name].
[1-2 culturally respectful sentences]

Stay connected: www.ijmeer.com

#IJMEER #[FestivalHashtag] #AcademicCommunity
```

---

## 5. Volume Threshold (Future Enhancement)

When real-time trend APIs become available, implement:

```
trending_score = current_volume / (3_month_average_volume)
if trending_score > 1.5:
    generate_trending_post()
```

Currently, the system uses calendar-based triggers only.
