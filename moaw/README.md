# MOAW edition

`workshop.md` is the complete English MOAW edition of **From Commit to
Firmware**. It lives alongside the original static HTML workshop, in the same
repository. No new repository, copy, website deployment or hosting workflow is
required.

The original `site`, `site.zip`, examples, supporting scripts and firmware
project are unchanged. The MOAW edition uses MOAW's native navigation,
admonitions and code blocks instead of the site's CSS, JavaScript and
browser-local progress tracking.

## Content and maintenance

The fifteen sections follow this mapping. Step numbers are zero-based; they
are navigation positions, not lab numbers.

| Step | Original page under `site/` | MOAW section |
| --- | --- | --- |
| 0 | `index.html` | Introduction |
| 1 | `prerequisites.html` | Customer preflight |
| 2 | `labs/01-local-build.html` | Lab 1 |
| 3 | `labs/02-first-pipeline.html` | Lab 2 |
| 4 | `labs/03-tests-and-debugging.html` | Lab 3 |
| 5 | `labs/04-arm-firmware.html` | Lab 4 |
| 6 | `labs/05-quality-gates-optional.html` | Optional lab 5 |
| 7 | `labs/06-sbom-optional.html` | Optional lab 6 |
| 8 | `labs/07-versioned-releases.html` | Lab 7 |
| 9 | `deployment-concepts.html` | Required deployment discussion |
| 10 | `troubleshooting.html` | Troubleshooting |
| 11 | `workflow-examples.html` | Complete workflow examples |
| 12 | `solutions.html` | Solution reference |
| 13 | `extensions.html` | Optional extensions |
| 14 | `instructor.html` | Facilitator guide |

Keep labs 1-4, lab 7 and the deployment discussion as the core route.
The links after lab 4 skip the independent optional labs. MOAW's generic
Next button still follows document order, so the optional pages are clearly
labelled and include skip links.

When changing teaching content, update both editions. Keep commands and
`<!-- source: ... -->` fenced blocks aligned with their canonical files under
`examples`, `scripts`, `samples` and `.github/workflows/release.yml`; the
Python tests compare every source-marked block and its location in the
solution accordions. Do not edit an embedded copy without reviewing its source.
Anonymous command illustrations must also remain aligned with the HTML edition.

MOAW rewrites every unescaped `assets/` substring, including inside code fences
and in names such as `release-assets/`. The Markdown therefore uses MOAW's
documented `\assets/` escape in those literal paths. The renderer removes the
escape before displaying/copying the code; the tests compare that rendered
form against the canonical files. Copy code from MOAW, not from the raw
Markdown fences, and verify this behaviour whenever updating the renderer.

Separate MOAW pages with a blank line, `---`, and another blank line. Do not
insert that sequence inside code or foldable sections: MOAW splits the raw
document at those separators, even inside a fence. Keep `sections_title`
aligned with section order.

MOAW sets an HTML base URL at the application root, so a bare `?step=N` link
leaves the workshop route. Internal links therefore use MOAW's native `route`
variable, a `step=N` parameter and, when needed, a stable explicit
`#step-N-anchor`. The default route targets this repository on `main`; its
colon is percent-encoded because MOAW's default-variable syntax also uses a
colon. Each link carries the route override forward through `vars`.

For local preview, set `vars=route:workshop/workshop.md` as shown below. The
same document then works locally and on the published MOAW route without
custom JavaScript. These links are not intended for GitHub's Markdown viewer.
If changing the publication repository, branch or folder, update the default
route in all internal links too. Review all links if reordering sections.

No separate assets are currently required. If adding images or downloads,
put them under `moaw/assets/` and use `assets/...` links so MOAW can rewrite
them against the workshop source. Do not copy the original site's CSS or JS.

## Local checks and preview

From the repository root:

```powershell
python -m unittest discover -s tests -p test_moaw.py -v
python -m unittest discover -s tests -v
git diff --check
```

For the official MOAW preview, install the CLI if it is not already available
(requires Node.js 20 or later):

```powershell
npm install -g @moaw/cli
moaw serve moaw\workshop.md
```

Open the address printed by the CLI, adding the local route override:

```text
http://localhost:4444/workshop/workshop.md?vars=route:workshop/workshop.md
```

Check page navigation, optional-module skip links, fragment links, tables,
YAML blocks, copy buttons and nested solution/reference accordions. The
route override is for local preview only; the public workshop link uses the
default route. An ordinary Python static server does not render this Markdown
as a MOAW workshop.

The existing firmware CI discovers the new Python tests automatically.
Changes under `moaw/**` trigger that same CI, including its existing reference
firmware builds. No new jobs, permissions or release behaviour are introduced.

## Review before sharing

Review the diff, inspect `git status --short`, and confirm no build outputs,
dependency caches, credentials or customer content are included. Keep author
and contact metadata accurate. The current attribution uses the repository
owner's public GitHub handle and profile, rather than an invented name/email.
The duration metadata describes the existing core facilitation budget and
excludes preflight and optional modules.

`published: true` marks this edition as ready for catalogue submission. Use
`published: false` for draft review. This flag controls catalogue eligibility,
**not privacy**: the public Markdown and its direct MOAW link can already be read.
Local validation is not evidence that an unpushed hosted version works.

## Share directly from this repository

Only after explicit approval to commit and push the reviewed changes:

1. Publish the approved files to the intended branch of this repository.
   Do not copy the workshop into a new repository.
2. Generate its link using the actual published branch, for example:

   ```powershell
   moaw link moaw\workshop.md -b main
   ```

3. Open the generated link and check the hosted workshop, including all
   sections, links, code blocks and resources. GitHub content caching can
   delay updates.
4. Share the verified link. Leave `published: false` if catalogue listing is
   not requested.

The source for the current intended location is:

```text
gh:ChristopheGigax-Microsoft/gh-actions-embedded-workshop/main/moaw/
```

The corresponding **target link** is
<https://aka.ms/ws?src=gh:ChristopheGigax-Microsoft/gh-actions-embedded-workshop/main/moaw/>.
It cannot serve the new edition until the files have been pushed to that
branch. Use the CLI to confirm it rather than assuming a hosted preview exists.

Use the official short links:
[MOAW](https://aka.ms/moaw) and the CLI-generated `https://aka.ms/ws?src=...`.
MOAW's upstream README announces the retirement of `moaw.dev` in 2027; do not
hardcode that domain in new workshop links.

## Optional catalogue registration

Direct hosting and catalogue registration are different:

1. After hosted review and explicit publication approval, set `published: true`
   and publish that metadata update.
2. Follow the official authoring guide to propose an entry in
   `packages/database/external.yml` in `microsoft/moaw`. Use the verified
   workshop link, repository URL, language `en`, metadata and actual update date.
3. Wait for the maintainers' review. A metadata change alone does not register
   the workshop.

A catalogue contribution may require a fork of **MOAW's** repository, not a
replacement or copy of this workshop repository. No catalogue contribution
is necessary for direct-link delivery.

The current workshop repository is public, so no external copy is needed.
If a later policy requires a different public destination, the repository
owner can copy the approved content themselves and regenerate the source
link. Recheck all assets and hosted links against that destination.

## References

- [Official authoring tutorial](https://github.com/microsoft/moaw/blob/main/workshops/create-workshop/workshop.md)
- [Metadata template](https://github.com/microsoft/moaw/blob/main/template/workshop/workshop.md)
- [CLI reference](https://github.com/microsoft/moaw/blob/main/packages/cli/README.md)
- [Upstream link guidance](https://github.com/microsoft/moaw/blob/main/README.md)
- [Format example supplied for this migration](https://github.com/Justrebl/AI-SDLC-Workshop/blob/main/docs/afternoon-2/workshop.md)
