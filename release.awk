# Set the library name when a symbol list starts and print the header
/^lvp_symbols = \[/ {
  lib="lvp"
  print "## `tinymesa_lvp.so` Symbols"
  next
}

/^nak_symbols = \[/ {
  lib="nak"
  print "\n## `tinymesa_nak.so` Symbols"
  next
}

# Unset the library name when a list ends
/^]/ {
  lib=""
}

# If we are inside a list, extract and print the symbol
lib != "" && /'/ {
  # Remove leading whitespace, quotes, and trailing comma
  sub(/^[ \t]+/, "")
  gsub(/[' ,]/, "")
  print "- " $0
}
