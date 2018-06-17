(ns gola.core
  (:gen-class))

(defn kk
  []
  (when (> 5 3)
    (println "lolalolalo")
    (println "blah blah perfection!")
    "shy")
  )

(defn hola
  [sev]
  (println
   (str "oh god we are in a "
        (if (= sev :mild)
          "slight problemum"
          "great dangeru!"
          )
        " because severity is " sev )))
(defn destaf
  [[first & rest]]
  (do
    (println (str "First:" first))
    (println (str "Rest:" rest))))

(defn maf
  "3 arg function"
  (
   [a1 a2 a3]
   println (str "3 args " a1 " " a2 " " a3))
  ;; ([a1 a2]
  ;;  println (str  "2 args " a1 " " a2))
  )

(defn pn [name]
  println (str "Hello " name))

(defn vaf [num & names]
  (do
    (println (str num " args passed!"))
    (map pn names)))
(defn mdf [{:keys [lat lon] :as lst}]
  (println (str "Latitude: " lat " Longitude:" lon))
  (println lst)
  "")

(defn golabola []
  (println "Anonymity!")
  (
   (fn [name & rest]
     (println (str "Name" name))
     (map (fn [n] (str "=>" n)) rest)) :a :b :c)
  )
(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  ( do (println "Hello, World!")
   (hola :mild) ))

(defn symmetrisize
  [abps]
  (loop [abps abps final_parts []]
    (if (empty? abps)
      final_parts
      (let [[cur & rem] abps]
        (recur rem (into final_parts (set [cur (mp cur)]) ))))))

(def abhp [
           {:name "head" :size 3}
           {:name "left-eye" :size 1}
           {:name "left-ear" :size 1}
           {:name "mouth" :size 1}
           {:name "nose" :size 1}
           {:name "neck" :size 2}
           {:name "left-shoulder" :size 3}
           {:name "left-upper-arm" :size 3}
           {:name "chest" :size 10}
           {:name "back" :size 10}
           {:name "left-forearm" :size 3}
           {:name "abdomen" :size 6}
           {:name "left-kidney" :size 1}
           {:name "left-hand" :size 2}
           {:name "left-knee" :size 2}
           {:name "left-thigh" :size 4}
           {:name "left-lower-leg" :size 3}
           {:name "left-achilles" :size 1}
           {:name "left-foot" :size 2}
           ]
  )


(defn mp [part]
  {
   :name (clojure.string/replace (:name part) #"^left-" "right-")
   :size (:size part)})

(defn makeparts
  [res prt]
   (into res (set [prt (mp prt)])) )

(defn symsz
  [abps]
  (reduce makeparts nil abps))
