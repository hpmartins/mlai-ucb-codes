### What drives the price of a car?

#### Findings

My analysis of this large dataset of used cars has revealed factors that significantly influence pricing, offering actionable guidance for inventory and sales strategies.

- **Mileage (odometer)**: The odometer reading is the most critical predictor, with higher mileage leading to lower prices. Each additional 1000 miles is associated with a $400 decrease in price.
- **Vehicle Type**: Trucks and offroad vehicles tend to have higher prices, while sedans and hatchbacks are associated with lower prices.
- **Vehicle Condition**: Cars in better condition command higher prices, with each increase in the condition level associated with around $10000 increase in the price.
- **Fuel Type**: Diesel cars generally command higher prices than gasoline cars.
- **Vehicle Age**: Older vehicles depreciate, leading to lower prices. Each additional year of age is associated with around $2400 decrease in the price.
- **Cylinders**: Vehicles with 8 or 12 cylinders tend to have higher prices, while those with 3, 4, or 5 cylinders are associated with lower prices.
- **Brands**:
  - *High-value brands*: Morgan, Ferrari, and Datsun vehicles significantly increase a car's predicted value. A Morgan vehicle is predicted to be much more expensive than the baseline model, all else being equal. This translates to a potential price increase of thousands of dollars.
  - *Low-value brands*: Saturn, Mercury, Fiat, Mitsubishi, Chrysler, Dodge, Kia, Land Rover, Nissan, and Mazda vehicles tend to decrease the predicted value compared to a baseline.
- **Title status impact**:
  - *Negative impact*: Cars with "parts only" or "missing" titles significantly reduce predicted value due to their limited usability and potential legal issues.
  - *Positive impact*: A "clean" title is the most desirable, increasing the predicted value due to the car's clear history and ownership. A "lien" title also increases the predicted value, potentially due to the car being associated with financing, which some buyers might prefer.
  
#### Next steps

- Ignore odometer and check model, paint color, manufacturer more closely
