check_status = ['idle', 'delivering', 'charging']


class Package:
    def __init__(self, packageId, weightInKg):
        self.packageId = packageId
        self.weightInKg = weightInKg


class Drone:
    def __init__(self, droneId, maxLoadInKg, status):
        self.droneId = droneId
        self.maxLoadInKg = maxLoadInKg
        self.__status = status
        self.assigned_package = None
        self.delivery_timer = 0

    def get_status(self):
        return self.__status

    def set_status(self, newStatus):
        if newStatus.lower() not in check_status:
            print("Enter valid status")
            return
        self.__status = newStatus.lower()

    def assign_package(self, packageObj):
        if self.__status == 'idle' and packageObj.weightInKg <= self.maxLoadInKg:
            self.assigned_package = packageObj
            self.set_status('delivering')
            self.delivery_timer = 2 
            print(f"Drone {self.droneId} assigned package {packageObj.packageId}")
            return True
        else:
            print(f"Drone {self.droneId} cannot take package {packageObj.packageId}")
            return False


class FleetManager:
    def __init__(self):
        self.drones = {}
        self.pending_packages = []
        self.current_pkg_index = 0  #

    def add_drone(self, droneId, maxLoadInKg, status):
        index = len(self.drones)
        self.drones[index] = Drone(droneId, maxLoadInKg, status)

    def add_package(self, packageObj):
        self.pending_packages.append(packageObj)

    def dispatchJobs(self):
    
        for drone in self.drones.values():
            if (drone.get_status() == 'idle' and 
                self.current_pkg_index < len(self.pending_packages)):
                
                pkg = self.pending_packages[self.current_pkg_index]
                if drone.assign_package(pkg):
                    self.current_pkg_index += 1

    def simulationTick(self):
        for drone in self.drones.values():
            if drone.get_status() == 'delivering':
                drone.delivery_timer -= 1
                if drone.delivery_timer <= 0:
                    drone.assigned_package = None
                    drone.set_status('charging')
            elif drone.get_status() == 'charging':
                drone.set_status('idle')



packages = [
    Package(3412, 10),
    Package(3532, 6.4),
    Package(4523, 2.5),
    Package(3112, 7.3),
    Package(6456, 8)
]

fm = FleetManager()
fm.add_drone(6543, 10, 'idle')
fm.add_drone(9041, 5, 'charging')
fm.add_drone(4523, 8, 'delivering')
fm.add_drone(4745, 6, 'idle')

for pkg in packages:
    fm.add_package(pkg)

fm.dispatchJobs()
fm.simulationTick()
