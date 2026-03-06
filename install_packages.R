packages <- readLines("/tmp/packages.txt")
install.packages(packages, repos = "https://cloud.r-project.org")
