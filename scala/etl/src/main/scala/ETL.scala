object ETL {

  type Points = Int
  type Letter = String
  // Old data structure:
  //   -> Map(p1->Seq(l_1,l_2,...,l_l),...,pm->Seq(l_{l+m},...,l_n))
  //   -> each element is a pair Points -> Seq[Letter]
  type OldData = Map[Points,Seq[Letter]]
  // New data structure:
  //   -> Map(l_1->p_1,...,l_n->p_n)
  //   -> each element is a pair Letter -> Points
  type NewData = Map[Letter,Points]
  // Strategy:
  //   -> for each pair (p: Points, ls: Seq[Letter]) in the old data structure,
  //      loop over each l in ls, yeilding a pair (l, p)---i.e. an element of
  //      the new data structure
  //        |-> for comprehension takes the Map in the old data style and
  //            generates a Map in the new data style
  def transform(od: OldData): NewData =
    for ((p, ls) <- od; l <- ls) yield (l.toLowerCase, p)

}