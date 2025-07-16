import subprocess
paths = [
    "",
    "/About-Us",
    "/Contacts",
    "/Our-Clients",
    "/Privacy-Policy",
]
for p in paths:
    url = "https://"+"mindtapp.com" + p
    args = ['curl', '-k', url, '-o', "." + p + "/index.html"]
    print(" ".join(args))
    subprocess.run(args)
