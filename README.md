**After checking files availability**


## Final Step: Standardized File Renaming

After completing the availability check, the script performs a final normalization pass to rename all annual report files into a strict, uniform naming format. This ensures downstream compatibility and consistent archival.

### Required Directory Structure

Before running this step, all previously **checked** company folders must be placed inside a parent directory named:

```
AnnualReports
```

Each company folder should still follow the established naming pattern:

```
<BSE Code> <Symbol>
```

### Required Excel Input

The script also expects an Excel file containing metadata for each company. This file must include at least the following two columns:

* `co_code` — the **BSE code** for the company
* `nse_symbol` — the **NSE symbol** for the company

These identifiers are used to correctly map each folder to its BSE code and perform accurate renaming.

### What the Script Does

1. It loads the metadata Excel file.
2. It scans every company folder inside the **AnnualReports** directory.
3. For each folder, it reads all annual report files previously downloaded (e.g., `RELIANCE 2021.pdf`).
4. It extracts the reporting year from each filename.
5. It renames every file using the standardized format:

```
<BSE Code>_AR_<Year>0331.pdf
```

Examples:

* `500325_AR_20250331.pdf`
* `532540_AR_20190331.pdf`

### Why “0331”

Most Indian listed companies follow a March 31 financial year-end. The suffix `0331` makes the date explicit, preserves chronological sorting, and avoids ambiguity in downstream systems.

### Output Characteristics

* All renamed files remain inside their respective company folders.
* No additional folders are created.
* Only the filenames change; the directory structure remains intact.

### Purpose

This final normalization step ensures:

* All reports follow an identical, machine-readable format.
* Sorting by filename mirrors sorting by financial year.
* Any downstream ingestion scripts or audit systems have consistent, predictable input.
