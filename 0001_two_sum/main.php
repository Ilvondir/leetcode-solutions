<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $my_nums = [];

        for ($i=0; $i < count($nums); $i++) {
            if (array_key_exists($nums[$i], $my_nums)) {
                array_push($my_nums[$nums[$i]], $i);
            }
            else {
                $my_nums[$nums[$i]] = [$i];
            }

            if (array_key_exists($target - $nums[$i], $my_nums) && $my_nums[$target - $nums[$i]][0] !== $i) {
                return [$i, $my_nums[$target - $nums[$i]][0]];
            }
        }
    }
}

$sol = new Solution();
echo $sol->twoSum([1, 2, 4, 5, 7], 7);

?>