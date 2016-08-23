import scala.collection.mutable
import scala.collection.immutable.SortedMap

class School {

  type Name = String
  type Grade = Int
  type Class = Seq[Name]
  type Roster = mutable.Map[Grade,Class]
  type FixedRoster = SortedMap[Grade,Class]

  private val theRoster: Roster = mutable.Map[Grade,Class]()
                
  def add(stuName: Name, grNum: Grade): Unit = {
    lazy val emptyClass: Class = Seq[Name]()
    val updatedClass: Class =
      theRoster.getOrElseUpdate(grNum, emptyClass) :+ stuName
      theRoster.update(grNum, updatedClass)
  }
                  
  def grade(grNum: Grade): Class = theRoster.getOrElse(grNum, Nil).toSeq
                  
  def db: FixedRoster = SortedMap(theRoster.toSeq:_*)
                  
  def sorted: FixedRoster = db.mapValues(_.sorted)
                     
}