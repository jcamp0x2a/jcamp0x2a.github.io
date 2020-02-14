# Example 1 (point animation)
animated_plot3d(
    lambda t: point3d((sin(t), cos(t), sin(t)*cos(t)), size=20),
    t=anim_var([0,pi/16,..,2*pi], speed=pi)
)

# Example 1 (behind scenes of animated_plot3d and anim_var)
def mypoint(t, index):
    p = point3d((sin(t), cos(t), sin(t)*cos(t)), size=20)
    p.animation_keys({'t': index})
    return p
indices = list(range(0, 33))
ts = [i * pi/16 for i in indices]
g = sum([mypoint(t, index) for t, index in zip(ts, indices)])
g.animation_vars({'t': AnimationVariable(ts, speed=pi)})
show(g)

# Example 2 (parametric curve animation)
def myplot(t, ampl=1, x0=-2*pi, x1=2*pi):
    p1 = parametric_plot3d([ampl*sin(x-t),0,x], (x,x0,x1), color='red')  
    p2 = parametric_plot3d([0,-ampl*sin(x-t),x], (x,x0,x1), color='green')
    return p1 + p2
curve_plot = animated_plot3d(myplot, ampl=2, t=anim_var(0,pi/16,..,2*pi))
show(curve_plot, projection='orthographic')

# Example 3 (surface animation with multiple animation variables)
var('theta,phi')
def draw_torus(R, r):
    return parametric_plot3d(
        [(R + r*cos(theta)) * cos(phi), (R + r*cos(theta)) * sin(phi), r*sin(theta)],
        (theta,0,2*pi), (phi,0,2*pi))
animated_plot3d(draw_torus, R=anim_var(0.2,0.4,..2), r=anim_var(0.2,0.4,..,2))

# Example 4 (animate3d similar to the regular animate; takes a list of frames)
animate3d([point3d((x,sqrt(x),x^2), size=20) for x in xsrange(0,2,0.1)], delay=5, loop='pingpong')
