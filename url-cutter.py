def cut_url(url):
	base_url = url.split("/products")[0]
	return base_url

with open("clipboard_log.txt", "r") as f:
	urls = f.read().splitlines()

cut_urls = [cut_url(url) for url in urls]

with open("cut_urls.txt", "w") as f:
	f.write("\n".join(cut_urls))

print("URLs are cut and served.")