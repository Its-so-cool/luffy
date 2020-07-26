<template>
    <div class="home">
        <Head></Head>
        <Banner></Banner>
        <div>
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        </div>
        <Footer></Footer>

    </div>
</template>

<script>
    import Head from "../components/Head";
    import Footer from "../components/Footer";
    import Banner from "../components/Banner";

    export default {
        name: 'Home',
        data() {

        },

        components: {
            Head,
            Footer,
            Banner
        },


    }
</script>
