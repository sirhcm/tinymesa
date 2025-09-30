/^lvp_symbols = \[/ {
  lib="lvp"
  print "## `libgallium` Symbols"
  next
}

/^nak_symbols = \[/ {
  lib="nak"
  print "\n## `libnak` Symbols"
  next
}

/^]/ { lib="" }

lib != "" && /'/ {
  sub(/^[ \t]+/, "")
  gsub(/[' ,]/, "")
  print "- " $0
}
