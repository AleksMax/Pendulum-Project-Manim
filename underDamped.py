from manim import *
from math import sin, cos, sqrt, exp

class underDamped(Scene):
    def construct(self):
        # Initialise variables as animation variables
        time = ValueTracker(0)
        initThetaVal = PI/9
        initTheta = Variable(initThetaVal, r'\theta')

        l = 5 # Length
        g = 50 # Gravity
        b = 0.2 # Damping
        w = np.sqrt(((g/l)**2)+(b**2)) # Damped Omega
        p = 2*PI/w # Period

        # Set Center of Pendulum
        originX = -4
        originY = 2.75
        startPoint = Dot([originX, originY, 0], radius=0.1, color=WHITE)
        originShft = originX* RIGHT + originY * UP

        # Vary Theta by function
        theta = DecimalNumber().shift(10*UP)
        theta.add_updater(lambda m: m.set_value(initTheta.tracker.get_value()*np.exp(-b*time.get_value())*np.sin(w*time.get_value())))
        self.add(theta)

        # Generate line
        def getLine(x, y):
            line = Line(start=ORIGIN + originShft, end=x*RIGHT+y*UP+originShft, color=WHITE)
            return line

        # Generate pendulum ball
        def getEndBall(x, y):
            endBall = Dot(fill_color=WHITE, fill_opacity=1).move_to(x*RIGHT+y*UP+originShft).scale(l)
            return endBall

        # Redraw pendulum for every frame
        line = always_redraw(lambda: getLine(l * np.sin(theta.get_value()), -l * np.cos(theta.get_value())))
        ball = always_redraw(lambda: getEndBall(l * np.sin(theta.get_value()), -l * np.cos(theta.get_value())))        
        
        # Equations
        eq1 = MathTex(r"\ddot{\theta}+2b \dot{\theta}+\omega^{2} \theta=0 \nonumber")
        eq2 = MathTex(r"\alpha^{2}+2b \alpha+\omega^{2}=0 \nonumber")
        eq3 = MathTex(r"\alpha_{\pm}=-b \pm \sqrt{b^{2}-\omega^{2}} \nonumber")
        eq4 = MathTex(r"\nonumber \gamma=\sqrt{\omega^{2}-b^{2}} \nonumber")
        eq5 = MathTex(r"\nonumber \alpha_{\pm}=-b \pm i \gamma \nonumber")
        eq6 = MathTex(r"\nonumber \theta(t)=e^{-bt}\left(A \cos \gamma t+B \sin \gamma t\right) \nonumber")

        # Align equations to bottom right
        eq = VGroup(eq1,eq2,eq3,eq4,eq5,eq6)
        eq.to_edge(DR)

        # Shift equations upwards
        j = 2.95
        for i in eq:
            i.shift(j*UP)
            j-= 0.65

        # Generate axis and align graphs to top right corner
        axis = Axes(x_range = [0, 13, 5], y_range= [-PI/9,PI/9,PI/9], x_length= 7, y_length = 3, axis_config={"include_tip": True, "exclude_origin_tick": True, "tip_width": 0.1, "tip_height": 0.1})
        axis.to_edge(UR)
        axis_labels = axis.get_axis_labels(x_label = "t", y_label = r'\theta')
        graph = always_redraw(lambda : axis.plot(lambda x: (PI/9)*np.exp(-b*x)*np.sin(w*x), x_range = [0, time.get_value(), 0.01], color = GREEN)) # Redraw graph for every frame

        self.play(Create(VGroup(startPoint, line, ball)), DrawBorderThenFill(axis), Write(axis_labels), Create(eq)) # Draw all objects

        self.play(Create(graph)) # Draw Graph Line
        self.play(time.animate.set_value(20*p), rate_func=linear, run_time=37) # Number of oscillations, linear time run, 37 seconds total