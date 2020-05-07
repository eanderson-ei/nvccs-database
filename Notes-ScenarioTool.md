# README

Nevada CCS Scenario Tool

Requirements:

* Take as input the current site values table from a database
* For each of 3 pre-defined scenarios, manipulate the current values up or down to reflect expected changes for high, medium and low efforts (this results in 12 tables)
* For each of 9 tables above, input the predicted df into the scoring algorithm to get site scores for projected condition
* For each of 9 site scores above, input into credit algorithm to get credits



Scenarios

1. Control cheatgrass
2. Enhance forb and grass component
3. Enhance shrub component



Also need to show credits resulting from conifer removal, although it is required so it is not a scenario

* Take as input the current and predicted condition
* Calculate credits from current as normal
* Calculate credits from predicted local scale and current site scale (ignoring site-scale uplift to get only credits resulting from conifer removal or anthro removal)



Import calc_credits.py

Read in site_scale values, desktop_results, standard_baseline

#current for comparison

run score_site_scale to get current site scale

run calc facres to get current facres report

#scenarios

for each scenario

​	for each effort level

​		#create tidy projected site scale based on scenarios, max at 1, min at 0

​		run project_site_scale to burn projected site scale into current

​		run score_site_scale to get projected site scale scores

​		run calc_facres to get f-acre report

​		run calc_credits to get credits relative to current facres report

​		return dict of form {scenario_effort: df}

#conifer

run correct_baseline to correct baseline

run baseline_facres to get baseline facre report

run calc facres with current_site_scale and projected_ls

run calc_credits to get credits relative to current for projected_ls

​	(current vs. baseline is preservation, conifer vs. current is conifer, projected vs current is conifer plus site-scale improvements)

return conifer_only_df

TODO

- [x] calc_facres ignores projected condition, update to switch between current and projected (option 1: switch prefix from current to projected based on input parameter, option 2: break local scale scores into own table and join with desktop results)
- [x] Move data imports from calc_credits to new class in models called CreditData, include curve basenames as property
- [x] Add parameters to run_calculator function, return current_credits and projected_credits reports (site_scale_values, desktop_results, current_ls, projected_ls, standard baseline, projected_values)
- [x] Add output suffix to new function save_outputs, which takes a credit report and saves with suffix
- [x] delete and re-build database
- [x] develop scenario_testing.py framework (see above)
- [x] develop 3 scenario functions
- [ ] improve usage of CreditData class in credit_calc.py





