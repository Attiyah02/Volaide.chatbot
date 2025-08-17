import streamlit as st
import random
from datetime import datetime
import os

# Your existing bot class
class EnhancedHIVCareBot:
    def __init__(self):
        self.responses = {
            "disclosure": {
                "primary": [
                    "**HIV Disclosure Support:** Create a safe, private environment where the person feels comfortable. Use simple, age-appropriate language and give them time to process emotions. Consider involving a trusted counselor or supportive family member. Remember - disclosure is a gradual process, not a single conversation.",
                    
                    "**Disclosure Strategy:** Help them identify their strongest support person first. Practice the conversation beforehand if they're nervous. Prepare for different reactions and have resources ready to share. Follow up within a few days to provide continued emotional support.",
                    
                    "**Teen Disclosure Tips:** For adolescents, timing is crucial - choose when they feel emotionally ready. Discuss potential reactions and coping strategies. Emphasize that their HIV status doesn't define their worth. Connect them with peer support groups of other young people living with HIV."
                ],
                "follow_up": [
                    "Would you like specific guidance on disclosure to family, friends, or romantic partners?",
                    "Are you looking for resources to help someone prepare for disclosure conversations?",
                    "Do you need information about disclosure support groups in your area?"
                ]
            },
            
            "medication": {
                "primary": [
                    "**Medication Adherence Strategies:** Establish consistent daily routines by linking pill-taking to existing habits (meals, bedtime). Use pill organizers and phone alarms. Address side effects immediately with healthcare providers. Create accountability with treatment buddies or family support.",
                    
                    "**ARV Success Tips:** Take medications at exactly the same time daily - this maximizes effectiveness. Never skip doses, but if you miss one, take it as soon as you remember (unless it's almost time for the next dose). Keep a backup supply when traveling.",
                    
                    "**Treatment Support System:** Build a network including healthcare providers, family, friends, or peer supporters. Regular viral load monitoring shows treatment success. Celebrate adherence milestones - 30 days, 3 months, 6 months. Address barriers like transport to clinics or medication costs."
                ],
                "follow_up": [
                    "Are you dealing with specific medication side effects that need addressing?",
                    "Do you need help creating a medication routine that fits your lifestyle?",
                    "Would you like information about medication assistance programs?"
                ]
            },
            
            "grief": {
                "primary": [
                    "**Grief & Emotional Support:** Grieving after HIV diagnosis is completely normal and healthy. Allow yourself to experience all emotions - anger, sadness, fear, hope. Professional counseling provides safe space to process these feelings. Connect with others who truly understand your experience.",
                    
                    "**Coping Strategies:** Focus on what you can control - treatment adherence, healthy lifestyle choices, building support systems. Challenge negative self-talk about HIV. Practice stress management through exercise, meditation, or creative activities. Set small, achievable goals for the future.",
                    
                    "**Building Resilience:** Join support groups to share experiences and learn from others. Maintain social connections - isolation worsens grief. Engage in meaningful activities that bring purpose. Remember: people with HIV live full, healthy, successful lives with proper care and support."
                ],
                "follow_up": [
                    "Are you looking for professional counseling resources in your area?",
                    "Would you like help connecting with peer support groups?",
                    "Do you need strategies for dealing with HIV-related stigma or discrimination?"
                ]
            },
            
            "resources": {
                "primary": [
                    "**Key South African HIV Resources:**\n• **National AIDS Helpline:** 0800 012 322 (free, confidential)\n• **Treatment Action Campaign (TAC):** Legal advocacy and support\n• **Mothers2Mothers:** Peer mentorship programs\n• **loveLife:** Youth-focused HIV prevention and support\n• **Provincial health clinics:** Free HIV testing and treatment\n• **Community health workers:** Local support and guidance",
                    
                    "**Youth-Specific Services:** Many clinics offer teen-friendly hours and private consultations. School-based health programs provide confidential support. NGOs like the AIDS Foundation focus specifically on adolescent needs. Peer education programs connect young people with similar experiences.",
                    
                    "**Getting Connected:** Contact your nearest public health clinic for medical care - ARVs are free in South Africa. Local NGOs provide psychosocial support, food assistance, and educational programs. Many services specifically designed for young people living with HIV."
                ],
                "follow_up": [
                    "Are you looking for resources in a specific province or city?",
                    "Do you need help accessing free HIV treatment through public clinics?",
                    "Would you like information about youth support programs in your area?"
                ]
            },
            
            "prevention": {
                "primary": [
                    "**HIV Prevention Education:** Use comprehensive, age-appropriate information about transmission routes. Emphasize that HIV is preventable through consistent condom use, regular testing, and PrEP for high-risk individuals. Address myths and misconceptions with factual information.",
                    
                    "**Safe Practices:** Promote regular HIV testing every 3-6 months for sexually active individuals. Encourage open communication about HIV status between partners. Support access to male and female condoms, and ensure people know how to use them correctly.",
                    
                    "**Community Prevention:** Reduce stigma through education and awareness campaigns. Support comprehensive sex education in schools. Advocate for accessible testing services and youth-friendly clinics in communities."
                ],
                "follow_up": [
                    "Do you need educational materials for prevention programs?",
                    "Are you looking for information about PrEP (pre-exposure prophylaxis)?",
                    "Would you like guidance on conducting HIV prevention workshops?"
                ]
            }
        }
        
        self.keywords = {
            "disclosure": ["disclose", "disclosure", "tell", "telling", "family", "parents", "friends", "sharing", "reveal", "coming out"],
            "medication": ["medication", "pills", "adherence", "treatment", "arv", "antiretroviral", "drugs", "medicine", "viral load"],
            "grief": ["grief", "sad", "depressed", "emotional", "support", "counseling", "feelings", "cope", "coping", "mental health", "anxiety"],
            "resources": ["help", "resources", "contact", "support", "services", "where", "clinic", "organization", "assistance"],
            "prevention": ["prevent", "prevention", "education", "awareness", "condom", "testing", "prep", "safe sex", "transmission"]
        }
        
        self.conversation_starters = [
            "I'm here to provide evidence-based HIV care guidance. What specific area can I help you with today?",
            "As an HIV support assistant, I can help with disclosure, treatment adherence, emotional support, or connecting you with resources. What would be most helpful?",
            "I specialize in HIV care support for adolescents and healthcare workers in South Africa. How can I assist you?"
        ]

    def get_response_category(self, message):
        message_lower = message.lower()
        scores = {}
        
        for category, keywords in self.keywords.items():
            score = sum(2 if keyword in message_lower else 0 for keyword in keywords)
            if any(phrase in message_lower for phrase in [f"{category} help", f"about {category}", f"{category} support"]):
                score += 3
            if score > 0:
                scores[category] = score
        
        return max(scores, key=scores.get) if scores else "general"

    def generate_response(self, message, conversation_history=None):
        category = self.get_response_category(message)
        
        if category == "general":
            return random.choice(self.conversation_starters)
        
        response = random.choice(self.responses[category]["primary"])
        
        message_lower = message.lower()
        
        if "adolescent" in message_lower or "teenager" in message_lower or "teen" in message_lower:
            response += "\n\n*Note: For adolescents, always use age-appropriate approaches and involve trusted adults when necessary.*"
        
        if "urgent" in message_lower or "emergency" in message_lower:
            response = "🚨 **For medical emergencies, contact your healthcare provider immediately or call emergency services.**\n\n" + response
        
        if any(word in message_lower for word in ["guidelines", "official", "who", "clinical", "medical"]):
            response += "\n\n📋 **Clinical Reference:** WHO guidelines provide evidence-based medical protocols for HIV care and treatment."
        
        follow_ups = self.responses[category].get("follow_up", [])
        if follow_ups:
            response += f"\n\n💭 {random.choice(follow_ups)}"
        
        if category != "resources":
            response += "\n\n📞 **Remember:** For immediate support, contact the National AIDS Helpline: 0800 012 322"
        
        return response

# Initialize the bot
@st.cache_resource
def load_bot():
    return EnhancedHIVCareBot()

# Page configuration
st.set_page_config(
    page_title="Voluide - HIV Support Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .main-header h1 {
        color: #2c3e50;
        font-size: 2.5em;
        font-weight: 700;
        margin-bottom: 10px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .main-header p {
        color: #7f8c8d;
        font-size: 1.2em;
        font-weight: 400;
        margin: 0;
    }
    
    .emergency-box {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0 10px 25px rgba(255, 107, 107, 0.3);
    }
    
    .emergency-box h4 {
        margin-top: 0;
        font-size: 1.3em;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #4834d4, #686de0);
        color: white;
        padding: 15px;
        border-radius: 12px;
        margin: 8px 0;
        text-align: center;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
    }
    
    .example-button {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        color: white;
        text-align: left;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .example-button:hover {
        background: rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.5);
        transform: translateY(-2px);
    }
    
    .chat-input-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .footer-info {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
        color: white;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Custom button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Chat message styling */
    .stChatMessage {
        border-radius: 15px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
    }
    
    .stChatMessage[data-testid="chat-message-user"] {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }
    
    .stChatMessage[data-testid="chat-message-assistant"] {
        background: rgba(255, 255, 255, 0.95);
    }
</style>
""", unsafe_allow_html=True)

# Load bot
bot = load_bot()

# Header
st.markdown("""
<div class="main-header">
    <h1>🏥 Voluide HIV Support Assistant</h1>
    <p>Professional HIV care guidance powered by official health resources</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with features
with st.sidebar:
    st.markdown("### 🎯 Key Features")
    
    features = [
        "💬 Disclosure Support",
        "💊 Treatment Guidance", 
        "🤝 Emotional Support",
        "📍 Resource Connection",
        "📚 Prevention Education"
    ]
    
    for feature in features:
        st.markdown(f'<div class="feature-card">{feature}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="emergency-box">
        <h4>🚨 Emergency Contacts</h4>
        <p><strong>National AIDS Helpline</strong><br>
        📞 0800 012 322<br>
        <small>Free & Confidential 24/7</small></p>
        
        <p><strong>Emergency Services</strong><br>
        📞 10177 or 112<br>
        <small>Medical Emergencies</small></p>
        
        <p><strong>Crisis Support</strong><br>
        📞 0800 567 567<br>
        <small>Mental Health Crisis Line</small></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="color: white; text-align: center; padding: 15px;">
        <h4>📚 Knowledge Base</h4>
        <p>✅ WHO Clinical Guidelines<br>
        ✅ Youth Care Resources<br>
        ✅ South African Health Data<br>
        ✅ Evidence-Based Protocols</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Example questions (show only if no conversation started)
if len(st.session_state.messages) == 0:
    st.markdown("### 💭 Try asking about:")
    
    examples = [
        "How can I help a teenager tell their parents about their HIV status?",
        "What are the most effective strategies for medication adherence?",
        "I'm struggling with grief after my HIV diagnosis - what support is available?",
        "What HIV resources and services are available in South Africa?",
        "How do I educate young people about HIV prevention?",
        "My patient is missing appointments - how can I help them stay on track?"
    ]
    
    # Create two columns for examples
    col1, col2 = st.columns(2)
    
    for i, example in enumerate(examples):
        with col1 if i % 2 == 0 else col2:
            if st.button(f"💡 {example[:50]}...", key=f"example_{i}", help=example):
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": example})
                
                # Generate response
                response = bot.generate_response(example)
                timestamp = datetime.now().strftime("%H:%M")
                response += f"\n\n---\n*Response generated at {timestamp} | Always consult healthcare professionals for medical decisions*"
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
                
                # Rerun to show the conversation
                st.rerun()

# Chat input
if prompt := st.chat_input("Ask me about HIV care support... 💬", key="chat_input"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            response = bot.generate_response(prompt)
            timestamp = datetime.now().strftime("%H:%M")
            response += f"\n\n---\n*Response generated at {timestamp} | Based on official health resources | Always consult healthcare professionals for medical decisions*"
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear conversation button
if len(st.session_state.messages) > 0:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Clear Conversation", key="clear_chat"):
            st.session_state.messages = []
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div class="footer-info">
    <h4>🏥 Voluide HIV Support Assistant</h4>
    <p>Developed for South African healthcare workers and communities</p>
    <p><small>This assistant provides evidence-based guidance from WHO clinical protocols and local health resources. 
    Always consult qualified healthcare professionals for medical decisions.</small></p>
    <p style="opacity: 0.7; margin-top: 15px;">© 2024 Voluide Project • Empowering HIV Care Through Technology</p>
</div>
""", unsafe_allow_html=True)