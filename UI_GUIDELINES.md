# UI_GUIDELINES.md — Design Rules for Agents

---

## CRITICAL: Do NOT change anything visual without explicit user approval.

---

## ✅ WHAT CAN BE CHANGED (Safe Zone)

| Element | Examples |
|---|---|
| **Text content** | Names, emails, addresses, bio text, descriptions |
| **Links and URLs** | Href values, anchor targets, email addresses |
| **New HTML sections** | Adding new content using EXISTING CSS classes only |
| **Profile images** | Swapping `src`/`srcset` to correct image paths |
| **Tab content** | Adding/editing content inside existing `ptab-panel` blocks |
| **Alt text** | Improving image accessibility descriptions |
| **Meta tags** | Title, description, OG tags, Twitter cards |
| **ISSN placeholders** | Updating `XXXX-XXXX` when actual numbers are received |
| **Aria labels** | Accessibility improvements |

---

## ❌ WHAT CANNOT BE CHANGED (Locked Zone)

| Element | Reason |
|---|---|
| **Color palette** | Brand identity — requires design approval |
| **Typography** | Font families, sizes, weights — brand consistency |
| **Spacing system** | Padding, margin, gap values — layout integrity |
| **Layout structure** | Grid, flexbox configurations — visual consistency |
| **Navigation menu** | Header nav links, order, structure |
| **Footer structure** | Footer content, layout, social links order |
| **CSS class names** | Changing class names breaks shared styles |
| **CSS variable values** | `--navy`, `--gold`, `--blue`, etc. |
| **Animation timings** | Transitions, keyframes |
| **Dark mode** | NOT to be added under any circumstances |
| **Component JS** | `components.js` shared across all pages |
| **Grid column counts** | `.profiles-grid`, `.links-grid`, etc. |

---

## Profile Card Structure (Reference Standard)

The **reference profile** is **Prof. (Dr.) Ashok L. Sunatkari** in `editorial-portfolio.html`.

Every profile card **MUST** follow this exact DOM structure:

```html
<div class="profile-section portfolio-reveal" id="[member-id]">
  <div class="profile-card">
    <div class="profile-card-accent [accent-class]"></div>
    <div class="profile-body">

      <!-- SECTION 1: Photo + Identity (horizontal) -->
      <div class="profile-top">
        <div class="profile-photo-wrap">
          <img width="400" height="400"
            srcset="[200w] 200w, [400w] 400w, [800w] 800w"
            sizes="(max-width: 480px) 200px, (max-width: 768px) 400px, 800px"
            src="[full-size]"
            alt="[Name] — [Role], IJMEER"
            class="profile-photo" loading="lazy">
          <div class="profile-photo-badge [badge-class]" title="[Role]">[emoji]</div>
        </div>
        <div class="profile-identity">
          <div class="profile-roles">
            <span class="profile-role-badge [role-class]">[Role Label]</span>
          </div>
          <h2 class="profile-name">[Full Name]</h2>
          <div class="profile-designation">[Designation]</div>
          <div class="profile-institution">
            <svg><!-- building icon --></svg>
            [Institution Name]
          </div>
          <div class="profile-stats">
            <div class="prs"><!-- stat item --></div>
          </div>
        </div>
      </div>

      <!-- SECTION 2: Divider -->
      <div class="profile-divider"></div>

      <!-- SECTION 3: Tab Navigation -->
      <div class="profile-tab-bar" role="tablist" aria-label="[Name] profile">
        <button class="ptab-btn active" role="tab" aria-selected="true"
          onclick="switchTab(this,'[key]','bio')">Biography</button>
        <!-- Additional tabs as needed -->
      </div>

      <!-- SECTION 4: Tab Panels -->
      <div class="ptab-panel active" id="[key]-bio">
        <div class="bio-text"><!-- content --></div>
      </div>
      <!-- Additional panels matching tabs -->

    </div>
  </div>
</div>
```

---

## Accent CSS Classes (Do Not Mix)

| Class | Color | Used For |
|---|---|---|
| `accent-eic` | Navy gradient | Editor-in-Chief |
| `accent-managing` | Blue gradient | Managing Editor |
| `accent-intl` | Emerald shimmer | International members |
| `accent-advisory` | Amber shimmer | Advisory board |
| `accent-m1` | Amber → Orange | Member 1 (Sunatkari) |
| `accent-m2` | Orange → Red | Member 2 (Yende) |
| `accent-m3` | Purple → Blue | Member 3 (Malviya) |
| `accent-m4` | Teal → Emerald | Member 4 (Salim Khan) |

---

## Badge & Role Classes

| Role | Photo Badge Class | Role Badge Class |
|---|---|---|
| Editor-in-Chief | `badge-eic` | `role-eic` |
| Managing Editor | `badge-managing` | `role-managing` |
| Editorial Board | `badge-member` | `role-member` |
| International | `badge-intl` | `role-intl` |
| Advisory | `badge-member` | `role-member` |

---

## Grid Layout Rules

- `.profiles-grid` → `grid-template-columns: 1fr` (SINGLE column — do NOT change to multi-column)
- `.profile-top` → `grid-template-columns: auto 1fr` (photo left, content right)
- All profile cards display as **full-width horizontal cards**
- The `.intl-spotlight` banner appears **after** `.profile-top` and **before** `.profile-divider` for international members only

---

## Image Path Conventions

```
images/editorial/                         # Core editorial board members
images/editorial/[name]-200w.webp         # Srcset 200w variant
images/editorial/[name]-400w.webp         # Srcset 400w variant
images/editorial/[name].webp              # Original full size

images/international_&_special_editorial_board/   # International members
images/advisory_board/                    # Advisory board members
```

---

## Responsive Breakpoints (Reference Only)

| Breakpoint | Behavior |
|---|---|
| `> 768px` | Full desktop layout |
| `≤ 768px` | Single column grid |
| `≤ 640px` | Profile photo stacks above identity |
| `≤ 480px` | Compact mobile layout |
