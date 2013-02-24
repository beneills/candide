(shell-command "wget -O - \"http://abu.cnam.fr/cgi-bin/
donner_html?candide3\" > \"/tmp/candide.txt\"")

(find-file "/home/ziarkaen/Dropbox/candide/candide.txt")

(switch-to-buffer "candide.txt")

(strip-html)

(query-replace-regexp "\\n" "qrr")
(query-replace-regexp "[\\»\\«]" "")
(query-replace-regexp "-\\{3,\\}" "")
(query-replace-regexp "\\<[[:upper:]']\\{2,\\}\\>" "")
(query-replace-regexp " *, *,[, ]*" " ")
