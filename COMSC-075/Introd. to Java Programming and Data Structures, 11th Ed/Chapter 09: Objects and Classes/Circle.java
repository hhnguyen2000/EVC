// Define the circle class with two constructors

public class Circle extends GeometricObject {
	private double radius;

	public Circle() {
		this.radius = 1.0;
	}

	public Circle(double radius) {
		this.radius = radius;
	}

	/** Return radius */
	public double getRadius() {
	    return radius;
	}

	/** Set a new radius */
	public void setRadius(double radius) {
	    this.radius = radius;
	}

	@Override /** Return area */
	public double getArea() {
	    return radius * radius * Math.PI;
	}

	/** Return diameter */
	public double getDiameter() {
	    return 2 * radius;
	}
	
	@Override /** Return perimeter */
	public double getPerimeter() {
	    return 2 * radius * Math.PI;
	}

	/* Print the circle info */
	public void printCircle() {
	    System.out.println("The circle is created " + getDateCreated() +
	      " and the radius is " + radius);
	}
	
	public void printArea() {
		System.out.printf("The area of the circle of radius %,.3f is %,.3f.\n", 
				radius, getArea());
	}
}
