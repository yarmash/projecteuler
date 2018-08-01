(define limit 1000)

(define (is-multiple-of-3-or-5? n)
  (or (= (remainder n 3) 0) (= (remainder n 5) 0)))

(define (sum-multiples n s)
  (cond ((= n limit) s)
        ((is-multiple-of-3-or-5? n) (sum-multiples (+ n 1) (+ s n)))
        (else (sum-multiples (+ n 1) s))))

(display (sum-multiples 1 0))
(newline)
