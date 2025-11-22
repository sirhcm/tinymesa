/^lvp_symbols = \[/ {
  lib="lvp"
  print "## `gallium` Symbols"
  next
}

/^nak_symbols = \[/ {
  lib="nak"
  print "\n## `nak` Symbols"
  next
}

/^ir3_symbols = \[/ {
  lib="nak"
  print "\n## `ir3` Symbols"
  next
}

/^]/ { lib="" }

lib != "" && /'/ {
  sub(/^[ \t]+/, "")
  gsub(/[' ,]/, "")
  print "- " $0
}
