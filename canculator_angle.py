import math

class Pixel_to_Angle:
    
    def px_to_degree(self, px_detection):
        cm_to_px = 240 / 23.64
        point = px_detection / cm_to_px
        return (math.atan2(point, 100) * 180 / math.pi)
    
    def px_plus(self, px_point): # แปลง 240 เป็น 0 และ 480 เป็น 240
        if px_point < 240:
            return 240 - px_point
        else:
            return px_point - 240

    def d_or_e(self, px): #  depertion หรือ eveletion
        if px < 240:
            return "TOP"
        else:
            return "DOWN"

if __name__ == '__main__':
     
    px =  400 # พิกเซลที่ตรวจหาได้

    a = Pixel_to_Angle()
    
    print(a.px_to_degree(a.px_plus(px)), a.d_or_e(px))