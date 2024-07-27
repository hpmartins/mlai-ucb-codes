# Module 5: Practical Application

## Will a Customer Accept the Coupon?

In this practical application assignment I analyzed a dataset that is available at UCI Machine Learning repository. The dataset was collected via a survey and it describes different driving scenarios, personal information and details about people and whether they would accepted a coupon to a specific place. The coupons were for one of these places: bar, coffee house, carry out & take away, restaurant under \$20, and restaurant between \$20 and \$50.

All code is in [this notebook](https://github.com/hpmartins/mlai-ucb-codes/blob/main/practical_applications/module_5/module_5_application.ipynb) in this repository.

### Findings

Here I show my findings about the *coffee house* coupons. Part of the analysis for the *bar* coupons is also done inside as part of the assigment as an example, but not listed here.

The acceptance rate for coffee house coupons is influenced by several factors:

- High Acceptance (70%+):
  - Young drivers (under 30) who visit coffee houses frequently, especially if they are not alone and are not headed somewhere urgently (72.6% to 79.2%)
  - Older drivers (30 or older) who are not alone and visit coffee houses frequently (71.5%)
  
- Moderate Acceptance (around 50%):
  - Drivers who are alone and are driving in the same direction as the coffee house (52.5%)
  - Drivers who are not alone and are driving in either direction (54.5% for the same direction and 57.9% for the opposite direction)

- Low Acceptance (below 50%):
  - Young drivers (under 30) who are alone and do not visit coffee houses frequently (35.1%)
  - Drivers who are alone and are driving in the opposite direction of the coffee house (39.4%)

Overall key factors:

- Frequency of coffee house visits is the most influential factor, with frequent visitors being much more likely to accept the coupon.
- Presence of passengers such as Friends or Partner also plays a significant role, increasing the acceptance rate
- Age and direction have a more moderate impact on acceptance.

These findings suggest that targeting frequent coffee house visitors who are likely to have passengers would be the most effective strategy for a coffee house coupon campaign, particularly if they are young (under 30) and not headed somewhere urgently.
