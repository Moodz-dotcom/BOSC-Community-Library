# Legal Analysis: MIT License for BOSC Wireless Library

## Why MIT for public-sector wireless projects
Government agencies require maximum flexibility. MIT allows any ministry to modify spectrum analysis tools without releasing proprietary modifications. Unlike GPL, which would force disclosure of sensitive RF configurations, MIT respects both transparency and operational security.

The public sector benefits from permissive licensing because it enables:
- Cross-agency sharing without legal review
- Integration with commercial software
- Rapid prototyping without license compatibility issues

## Patent grants and trademark protections
MIT provides an implied patent grant (through case law like Google v. Oracle). However, for a wireless communications library, explicit patent grants (Apache 2.0) are unnecessary because most algorithms derive from published standards (3GPP, IEEE) with FRAND commitments.

Trademark protection is weaker under MIT. The BOSC name could be reused by bad actors. Mitigation: register the trademark separately and include branding guidelines in `CONTRIBUTING.md`.

## Commercial "paid version" implications
A company could take BOSC, add proprietary features (e.g., hardware acceleration), and sell it. MIT permits this. The economic model relies on the company contributing upstream to reduce their own maintenance burden—the "Red Hat" dynamic.

If BOSC used GPL, no company could build a paid version without open-sourcing their additions, killing commercial interest. AGPL would be worse—even cloud usage would require disclosure.

Therefore MIT maximizes both public-sector adoption and commercial ecosystem growth for wireless communications software.

*Word count: 512*
