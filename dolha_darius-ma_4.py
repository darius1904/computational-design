#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 00:41:05 2025

@author: darius
"""

class Material:
    def __init__(self, name, density, cost_factor, co2_factor):
        self.name = name
        self.density = density          # kg/m3
        self.cost_factor = cost_factor  # €/kg
        self.co2_factor = co2_factor    # kgCO2/kg

    def cost_per_m3(self):
        return self.density * self.cost_factor

    def co2_per_m3(self):
        return self.density * self.co2_factor

    def __repr__(self):
        return f"<Material: {self.name}>"


class Component:
    def __init__(self, name, material, volume):
        self.name = name
        self.material = material
        self.volume = volume  # m³

    @property
    def mass(self):
        return self.material.density * self.volume

    @property
    def cost(self):
        return self.material.cost_per_m3() * self.volume

    @property
    def carbon(self):
        return self.material.co2_per_m3() * self.volume

    def describe(self):
        return (f"{self.name} | Material: {self.material.name} | "
                f"Volume: {self.volume:.2f} m³ | "
                f"Cost: €{self.cost:,.2f} | CO₂: {self.carbon:,.2f} kg")





class Column(Component):
    def __init__(self, material, height, radius):
        volume = 3.1416 * radius**2 * height
        super().__init__("Column", material, volume) #calling methods from the superclass
        self.height = height
        self.radius = radius


class Roof(Component):
    def __init__(self, material, area, thickness):
        volume = area * thickness
        super().__init__("Roof", material, volume)
        self.area = area
        self.thickness = thickness


class Facade(Component):
    def __init__(self, material, area, thickness, transparency=0.5):
        volume = area * thickness
        super().__init__("Facade", material, volume)
        self.area = area
        self.thickness = thickness
        self.transparency = transparency

    def describe(self):
        base = super().describe()
        return f"{base} | Transparency: {self.transparency:.2f}"




class Pavilion:
    def __init__(self, title, designer="Unknown"):
        self.title = title
        self.designer = designer
        self.components = []

    def add(self, component):
        self.components.append(component)

    def total_cost(self):
        return sum(c.cost for c in self.components)

    def total_carbon(self):
        return sum(c.carbon for c in self.components)

    def report(self):
        print(f"\nPavilion Design Report: {self.title}")
        print(f"Designed by: {self.designer}")
        print("-" * 60)
        for comp in self.components:
            print(comp.describe())
        print("-" * 60)
        print(f"Total Pavilion Cost: €{self.total_cost():,.2f}")
        print(f"Total Pavilion CO₂ Footprint: {self.total_carbon():,.2f} kg")
        print("-" * 60)




timber = Material("Timber", density=500, cost_factor=0.6, co2_factor=0.10) 
steel = Material("Steel", density=7850, cost_factor=1.2, co2_factor=1.9)
glass = Material("Glass", density=2500, cost_factor=0.9, co2_factor=1.5)

#create instances (objects) of the Material class —specific materials you can use to build components.




if __name__ == "__main__":
    pavilion = Pavilion("Parametric Pavilion", designer="A. Student")

    # Add architectural components
    pavilion.add(Column(timber, height=3.2, radius=0.15))   # 
    pavilion.add(Column(timber, height=3.2, radius=0.15))
    
    pavilion.add(Roof(steel, area=25, thickness=0.05))
    pavilion.add(Facade(glass, area=40, thickness=0.02, transparency=0.8))

    # Show design summary
    pavilion.report()
    
    print(pavilion.components[0].describe())