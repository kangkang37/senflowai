// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 更新页面内容
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
            element.placeholder = translations.en[key];
        } else {
            element.textContent = translations.en[key];
        }
    });

    // 添加平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // 添加页面加载动画
    document.body.classList.add('page-enter-active');

    // 添加滚动监听，实现渐入效果
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // 监听所有需要动画的元素
    document.querySelectorAll('.animate-on-scroll').forEach((el) => {
        observer.observe(el);
    });

    // 表单验证
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // 获取表单数据
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            // 简单的表单验证
            if (!data.name || !data.email || !data.message) {
                alert('Please fill in all required fields');
                return;
            }
            
            // 验证邮箱格式
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(data.email)) {
                alert('Please enter a valid email address');
                return;
            }
            
            // 这里可以添加发送表单数据的逻辑
            console.log('表单数据:', data);
            alert('Message sent! We will contact you soon.');
            this.reset();
        });
    }

    // 响应式导航栏
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }
});

// 添加页面离开前的提示
window.addEventListener('beforeunload', function(e) {
    const form = document.querySelector('form');
    if (form) {
        const formData = new FormData(form);
        const hasInput = Array.from(formData.values()).some(value => value.length > 0);
        
        if (hasInput) {
            e.preventDefault();
            e.returnValue = '';
        }
    }
}); 