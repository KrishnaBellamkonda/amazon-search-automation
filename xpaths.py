productElementXPath = "//div[contains(@class, 's-result-item s-asin')]"

# Data XPaths 
linksXPath = productElementXPath + "//div[contains(@class, 'a-section')]//h2/a"
priceXPath = productElementXPath +  "//span[contains(@class, 'a-price-whole')]"
titleXPath = productElementXPath + "//h2/a/span"
sizeBaseXPath = productElementXPath + "//span[@class='a-size-base']"

#reviewsXPath = productElementXPath + "//span[contains(@aria-label, 'out of')]"

# Next Button 
nextButtonXPath = "//a[contains(@class, 's-pagination-next')]"