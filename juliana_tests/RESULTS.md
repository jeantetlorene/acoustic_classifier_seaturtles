# Preliminary turtle pulse detection results

## Dataset

* 119 pulse vocalizations
* 173 negative examples

## CNN (random split)

* Accuracy ≈ 97 %
* Pulse recall ≈ 92 %

## Generalization benchmark 1

Train:

* IMB_05
* IMB_06

Test:

* IMB_07

Results:

* Accuracy = 90 %
* Pulse recall = 85 % (29/34)

## Generalization benchmark 2

Train:

* IMB_05
* IMB_07

Test:

* IMB_06

Results:

* Accuracy = 94 %
* Pulse recall = 94 % (49/52)

## Preliminary interpretation

These preliminary results suggest that pulse vocalizations share acoustic characteristics across individuals and that a simple CNN can generalize reasonably well to unseen individuals.
