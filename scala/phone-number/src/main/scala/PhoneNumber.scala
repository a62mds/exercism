class PhoneNumber(val rawNum: String) {

  val filteredNum: String = rawNum.filter(_.isDigit)
  val InvalidNum: String = "0000000000"

  val number: String = filteredNum.length match {
    case 10 => filteredNum
    case 11 => if (filteredNum.head == '1') filteredNum.tail else InvalidNum
    case _ => InvalidNum
  }

  val areaCode: String = number.substring(0,3)

  override def toString: String = 
    s"($areaCode) ${number.substring(3,6)}-${number.substring(6,10)}"

}
