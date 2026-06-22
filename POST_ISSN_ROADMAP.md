# POST_ISSN_ROADMAP.md — Post-Approval Indexing & Growth Roadmap

> **Activate this roadmap when ISSN numbers are officially received.**  
> Track progress in `REMINDERS.md` and `MEMORY.md`.

---

## Timeline Overview

```
ISSN Received
    │
    ▼
Phase 1 (Month 1-3)     → Foundation & Compliance
    │
    ▼
Phase 2 (Month 3-6)     → National & Regional Indexing
    │
    ▼
Phase 3 (Month 6-12)    → International Indexing
    │
    ▼
Phase 4 (Year 2+)       → Scale & Technology
```

---

## Phase 1: Foundation & Compliance (Month 1–3)

### Immediate Actions (Day 1-7)

- [ ] **Update ISSN placeholders** — Replace ALL `XXXX-XXXX` with actual ISSN numbers
  - Pages: index.html, journal.html, about-this-journal.html, archive.html, editorial-board.html, authors.html, footer (components.js)
  - Commit: `update: add official ISSN [XXXX-XXXX (print)] [XXXX-XXXX (online)]`

- [ ] **Update MEMORY.md** — Record ISSN receipt date and numbers

- [ ] **Social media announcement** — Use Template 6 (Milestone) from `SOCIAL_MEDIA.md`

### Month 1

- [ ] **Add individual DOIs via Zenodo**
  - Create a Zenodo community for IJMEER
  - Upload each published article
  - Assign DOIs to each article in archive
  - Update `archive.html` with DOI links

- [ ] **Add plain language summaries**
  - Each published article gets a 2-3 sentence summary
  - Improves discoverability and DOAJ compliance

- [ ] **Internal linking audit**
  - Verify all cross-page links work
  - Add "Related Articles" where applicable
  - Ensure sitemap.xml covers all pages

### Month 2-3

- [ ] **DOAJ application preparation**
  - Complete DOAJ questionnaire
  - Ensure all compliance requirements are met:
    - Copyright policy clear
    - CC BY 4.0 stated
    - APC information (free / Diamond OA) explicit
    - ISSN present
    - At least 5 research articles published
    - Regular publication schedule demonstrated

- [ ] **Google Scholar profile**
  - Create/verify Google Scholar profile for IJMEER
  - Ensure published articles appear in Scholar

---

## Phase 2: National & Regional Indexing (Month 3–6)

### UGC Care List Application

- [ ] **Requirements:**
  - ISSN (received)
  - Minimum 2 published issues
  - Complete editorial board with affiliations
  - Peer review policy documented
  - Ethical guidelines published
  - Grievance officer designated
  - No predatory indicators

- [ ] **Process:**
  1. Visit UGC Care portal
  2. Submit application with supporting documents
  3. Pay application fee (if applicable)
  4. Track application status

### Index Copernicus (ICI)

- [ ] **Register journal** at https://indexcopernicus.com
- [ ] **Submit evaluation request**
- [ ] **Provide:** ISSN, editorial board, published issues, policies

### EBSCO Discovery Service

- [ ] **Apply** at EBSCO publisher portal
- [ ] **Submit:** Journal metadata, sample issues, ISSN

### Indian Citation Index (ICI)

- [ ] **Register** at Indian Citation Index website
- [ ] **Submit** journal details and published articles

### CrossRef Membership (for DOIs)

- [ ] **Apply for CrossRef membership** (alternative to Zenodo DOIs)
- [ ] **Cost:** Annual fee based on publication volume
- [ ] **Benefit:** Official DOI prefix, metadata distribution

---

## Phase 3: International Indexing (Month 6–12)

### Scopus Application

- [ ] **Prerequisites:**
  - Minimum 2 published issues (ideally 4+)
  - Regular publication on schedule
  - International editorial board ✅
  - Strong peer review process ✅
  - English-language abstracts for all articles
  - No evidence of predatory practices
  - ISSN ✅

- [ ] **Process:**
  1. Submit via Scopus Source Evaluation (https://suggestor.step.scopus.com)
  2. Provide 3+ complete issues
  3. Editorial board CVs
  4. Peer review documentation
  5. Wait 12-18 months for evaluation

### Web of Science (Clarivate) Application

- [ ] **Prerequisites:**
  - Established publication record (1-2 years minimum)
  - Strong citation metrics
  - International authorship
  - Complete metadata

- [ ] **Process:**
  1. Submit via Web of Science Journal Evaluation
  2. Similar documentation as Scopus
  3. Evaluation period: 12+ months

### Other International Directories

- [ ] **ROAD (Directory of Open Access scholarly Resources)** — Register after ISSN
- [ ] **Sherpa Romeo** — Register copyright/OA policy
- [ ] **BASE (Bielefeld Academic Search Engine)** — Submit for crawling
- [ ] **CORE (COnnecting REpositories)** — Register

---

## Phase 4: Scale & Technology (Year 2+)

### Technology Enhancements

- [ ] **OJS (Open Journal Systems)** — Consider migrating to OJS for:
  - Automated submission workflow
  - Built-in peer review management
  - DOI integration
  - Metadata export (OAI-PMH)

- [ ] **API for libraries** — Enable programmatic access to article metadata

- [ ] **Mobile-responsive audit** — Ensure optimal mobile experience

- [ ] **Search functionality** — Add article search within the journal

### Content Growth

- [ ] **Increase frequency** — Consider quarterly (4 issues/year) if submission volume allows

- [ ] **Special issues** — Thematic issues on trending topics

- [ ] **Book review section** — Activate `book-reviews.html`

- [ ] **Conference proceedings** — Partner with academic conferences

### Metrics & Impact

- [ ] **Track citation metrics** via Google Scholar, Scopus, WoS
- [ ] **Calculate internal metrics:** acceptance rate, time-to-publication, geographic diversity
- [ ] **Annual report** — Publish editorial statistics

---

## Agency Orchestration Toolkit

For future automation and scaling:

| Tool / Agent | Purpose | Status |
|---|---|---|
| **Agency Agents** | Coordinated multi-agent task execution | Planned |
| **Ruflo** | Workflow automation for submission processing | Planned |
| **Hermes** | Communication orchestration (reviewer notifications, author updates) | Planned |
| **ECC** | Editorial Calendar & Content scheduling | Planned |
| **Ray** | Research Analytics & Impact tracking | Planned |

### Integration Points:
- Submission email → Ruflo → Assign reviewer → Hermes notification
- Published article → Ray → Track citations → ECC → Social media post
- Agency Agents → Orchestrate cross-tool workflows

> These are aspirational tools. Implementation depends on journal growth and technical resources.

---

## Success Metrics by Phase

| Phase | Success Criteria |
|---|---|
| **Phase 1** | ISSN updated, DOIs assigned, DOAJ applied |
| **Phase 2** | UGC Care listed, Index Copernicus registered |
| **Phase 3** | Scopus application submitted, 50+ published articles |
| **Phase 4** | Scopus indexed, 100+ articles, automated workflows |

---

## Key Contacts for Indexing

| Organization | URL | Notes |
|---|---|---|
| ISSN India | https://issn.org | For ISSN queries |
| DOAJ | https://doaj.org | Open access directory |
| UGC Care | https://ugccare.unipune.ac.in | Indian journal listing |
| Scopus | https://suggestor.step.scopus.com | Source evaluation |
| Clarivate (WoS) | https://clarivate.com | Journal evaluation |
| Index Copernicus | https://indexcopernicus.com | ICV evaluation |
| CrossRef | https://crossref.org | DOI registration |
| Zenodo | https://zenodo.org | Free DOI assignment |
