from creational.prototype.Prototype import Prototype
from creational.prototype.Website import Website

if __name__ == "__main__":
    site1 = Website(name="QA Minds", domain="qaminds.com", description="QA Minds Community", author="Blanca",
                    category="Community")
    prototype = Prototype()
    prototype.register("qaminds", site1)

    site2 = prototype.clone("qaminds", name="QA Minds Shop", domain="qaminds.shop.com", creation_data="2018-08-01")

    for site in (site1, site2):
        print(site)
    print(f"Site 1 id {id(site1)} != Site 2 id {id(site2)}")


