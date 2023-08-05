from ..utils.doe_formatters import short_name
from .aperture import Window


class DoeWall:
    def __init__(self, face):
        self.face = face

    def to_inp(self, space_origin):

        p_name = short_name(self.face.display_name)
        wall_typology = 'EXTERIOR' if str(
            self.face.boundary_condition) == 'Outdoors' else 'INTERIOR'

        constr = self.face.properties.energy.construction.display_name
        tilt = 90 - self.face.altitude
        azimuth = self.face.azimuth
        origin_pt = self.face.geometry.lower_left_corner - space_origin

        spc = ''
        obj_lines = []

        obj_lines.append('"{}" = {}-WALL'.format(p_name, wall_typology))
        obj_lines.append('\n  POLYGON           = "{}"'.format(p_name+' Plg'))
        obj_lines.append('\n  CONSTRUCTION      = "{}_c"'.format(short_name(constr, 30)))
        obj_lines.append('\n  TILT              =  {}'.format(tilt))
        obj_lines.append('\n  AZIMUTH           =  {}'.format(azimuth))
        obj_lines.append('\n  X                 =  {}'.format(origin_pt.x))
        obj_lines.append('\n  Y                 =  {}'.format(origin_pt.y))
        obj_lines.append('\n  Z                 =  {}'.format(origin_pt.z))
        if wall_typology == 'INTERIOR':
            if self.face.user_data:
                next_to = self.face.user_data['adjacent_room']
                obj_lines.append('\n  NEXT-TO           =  "{}"'.format(next_to))
            else:
                print(
                    f'{self.face.display_name} is an interior face but is missing '
                    'adjacent room info in user data.'
                )
        obj_lines.append('\n  ..\n')

        temp_str = spc.join([line for line in obj_lines])

        doe_windows = [
            Window(ap, self.face) for ap in self.face.apertures
        ]

        nl = '\n'
        if doe_windows is not None:
            for window in doe_windows:
                temp_str += window.to_inp() + nl
            return temp_str
        else:
            return temp_str

    def __repr__(self):
        return f'DOE2 Wall: {self.face.display_name}'
