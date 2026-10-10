#!/bin/bash
# Tag Crypto Banter videos by host via description. Pure yt-dlp, no LLM cost.
# Output (appended, resumable): <date>|<id>|<kyleflag>|<title>
# kyleflag: DOOPS (strong) | KYLE? (only "kyle" word) | other | ERR
# Usage: tag-host.sh <ids_file> <out_file> [parallelism]
#   ids_file lines: <id>|... or just <id>   (processed in file order)
set -u
ids_file="$1"; out="$2"; par="${3:-16}"
touch "$out"
tag_one() {
  local id="${1%%|*}"
  local line flag date rest title
  # Single fetch. Inspect ONLY the description opening (names the actual
  # presenter), NOT the full description (CB dumps every host's affiliate links).
  local raw opening
  raw=$(yt-dlp --no-warnings --skip-download \
    --print "%(upload_date)s@@%(id)s@@%(title)s@@%(description).240s" \
    "https://www.youtube.com/watch?v=$id" 2>/dev/null | tr '\n' ' ')
  if [ -z "$raw" ]; then echo "NA|$id|ERR|"; return; fi
  date="${raw%%@@*}"; rest="${raw#*@@}"; title="${rest#*@@}"; title="${title%%@@*}"
  opening="${raw##*@@}"
  if printf '%s' "$opening" | grep -iqE "kyledoops|\bdoops\b"; then flag=DOOPS
  elif printf '%s' "$opening" | grep -iqE "\bsheldon\b|\bran\b|\bchento\b|\bdylan\b|eric krown|\bfefe\b|\bcepryl\b|alessandro|tooker|\bpedro\b"; then flag=other
  elif printf '%s' "$opening" | grep -iqE "\bkyle\b"; then flag="KYLE?"
  else flag=other; fi
  title="${title//|/ }"
  echo "$date|$id|$flag|$title"
}
export -f tag_one
# resumable: skip ids already present in out
done_ids=$(cut -d'|' -f2 "$out" 2>/dev/null | sort -u)
cut -d'|' -f1 "$ids_file" | grep -vxF "$done_ids" 2>/dev/null \
  | xargs -P "$par" -I{} bash -c 'tag_one "$@"' _ {} >> "$out"
echo "total tagged now: $(wc -l < "$out")"
