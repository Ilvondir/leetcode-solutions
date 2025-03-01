<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function applyOperations($nums) {
        $zero_indexes = [];

        for ($i=0; $i<count($nums)-1; $i++) {

            if ($nums[$i] == 0) {
                $zero_indexes[] = $i;
                continue;
            }

            if ($nums[$i] == $nums[$i+1]) {

                if (count($zero_indexes)) {
                    $nums[array_shift($zero_indexes)] = 2*$nums[$i];
                    $nums[$i+1] = 0;
                    $nums[$i] = 0;
                    $zero_indexes[] = $i;
                }
                else {
                    $nums[$i] = 2*$nums[$i];
                    $nums[$i+1] = 0;
                }
            }
            else {
                if (count($zero_indexes)) {
                    $nums[array_shift($zero_indexes)] = $nums[$i];
                    $nums[$i] = 0;
                    $zero_indexes[] = $i;
                }
            }
        }

        if (count($zero_indexes)) {
            $nums[array_shift($zero_indexes)] = $nums[count($nums) - 1];
            $nums[count($nums) - 1] = 0;
        }

        return $nums;
    }
}

$sol = new Solution();
$nums = [1, 2, 5, 6, 6, 9, 0, 0, 1];
print_r($sol->applyOperations($nums));