<?php

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {

    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {

        $result = new ListNode(($l1->val + $l2->val) % 10);
        $current1 = $l1->next;
        $current2 = $l2->next;
        $current_result = $result;
        $transfer = (integer)(($l1->val + $l2->val) / 10);

        while (1) {

            if ($current1 != null && $current2 != null) {
                $current_result->next = new ListNode(($current1->val + $current2->val + $transfer) % 10);
                $transfer = (integer)(($current1->val + $current2->val + $transfer) / 10);

                $current1 = $current1->next;
                $current2 = $current2->next;
            }
            elseif ($current1 == null && $current2 != null) {
                $current_result->next = new ListNode(($current2->val + $transfer) % 10);
                $transfer = (integer)(($current2->val + $transfer) / 10);

                $current2 = $current2->next;
            }
            elseif ($current1 != null && $current2 == null) {
                $current_result->next = new ListNode(($current1->val + $transfer) % 10);
                $transfer = (integer)(($current1->val + $transfer) / 10);

                $current1 = $current1->next;
            }
            else {
                if ($transfer > 0) $current_result->next = new ListNode($transfer);
                break;
            }

            $current_result = $current_result->next;
        }

        return $result;
    }
}

?>