import graphics.rectangle as rect
import graphics.circle as cir
import graphics.threeD_graphics.cuboid as cub
import graphics.threeD_graphics.sphere as spr
length=int(input("Enter length for rectangle:"))
breadth=int(input("Enter breadth for rectangle:"))
print("Rectangle area:",rect.area(length,breadth))
print("Rectangle perimeter:",rect.perimeter(length,breadth))
r1=int(input("Enter radius for circle:"))
print("Circle area:",cir.area(r1))
print("Circle perimeter:",cir.perimeter(r1))
l=int(input("Enter length for cuboid:"))
w=int(input("Enter width for cuboid:"))
h=int(input("Enter height for cuboid:"))
print("Cuboid area:",cub.area(l,w,h))
print("Cuboid perimeter:",cub.perimeter(l,w,h))
r2=int(input("Enter radius for sphere:"))
print("Sphere area:",spr.area(r2))
print("Sphere volume:",spr.volume(r2))


