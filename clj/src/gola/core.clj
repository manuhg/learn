
(ns gola.core
  (:gen-class))

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
  ([a1 a2]
   println (str  " args " a1 " " a2))
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
