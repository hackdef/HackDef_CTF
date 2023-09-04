using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;


class Program
{
    static string GenerateRandomKeyFromSeed(Int32 seed, int keyLength)
    {
        const string chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

        Random random = new Random(seed);

        char[] keyArray = new char[keyLength];

        for (int i = 0; i < keyLength; i++)
        {
            keyArray[i] = chars[random.Next(chars.Length)];
        }

        return new string(keyArray);
    }

    static void PrintBytes(byte[] input)
    {
        for (int i = 0; i < input.Length; i++)
        {
            Console.Write("{0}-", input[i]);
        }
        Console.WriteLine();
    }
    static void Main()
    {
        bool star_chall = true;
        if (star_chall)
        {
            try
            {
                string originalText = "My_0ld_Fr13nd_D3S_1_M1ss_U";

                for (int seed = Int32.MinValue; seed <= Int32.MaxValue; seed++)
                {
   
                    //this is my ciphertext Cxbli/044FRhkleIJx1pV/eO7sA4CQzWeluNQ3Fhf64=
                    string key = GenerateRandomKeyFromSeed(seed, 8);

                    // Encrypt the text
                    string encryptedBytes = Encrypt(originalText, key);

                    if (encryptedBytes.Equals("Cxbli/044FRhkleIJx1pV/eO7sA4CQzWeluNQ3Fhf64="))
                    {
                        Console.WriteLine(key);
                        break;
                    }
                }

                //byte[] decryptedBytes = DecryptTextToBytes(encryptedBytes, key);
                //ingres the key with the next format hackdef{y0ur_k3y_is_[key]}

                //string enc = "Cxbli/044FRhkleIJx1pV/eO7sA4CQzWeluNQ3Fhf64=";

                //string dec = Decrypt(enc, key);

                //Console.WriteLine(dec);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.StackTrace);
            }
        }
        else
        {
            string errorMessage = "An error occurred. Please try again later.";

            Console.WriteLine(errorMessage);
        }

    }

    static byte[] EncryptTextToBytes(string plainText, string key)
    {
        using (DESCryptoServiceProvider desProvider = new DESCryptoServiceProvider())
        {
            desProvider.Key = Encoding.UTF8.GetBytes(key);
            desProvider.Mode = CipherMode.ECB; // Electronic Codebook Mode

            using (ICryptoTransform encryptor = desProvider.CreateEncryptor())
            using (MemoryStream msEncrypt = new MemoryStream())
            using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
            using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
            {
                swEncrypt.Write(plainText);
                swEncrypt.Close();
                return msEncrypt.ToArray();
            }
        }
    }

    static byte[] DecryptTextToBytes(byte[] plainText, string key)
    {
        using (DESCryptoServiceProvider desProvider = new DESCryptoServiceProvider())
        {
            desProvider.Key = Encoding.UTF8.GetBytes(key);
            desProvider.Mode = CipherMode.ECB; // Electronic Codebook Mode

            using (ICryptoTransform encryptor = desProvider.CreateDecryptor())
            using (MemoryStream msEncrypt = new MemoryStream())
            using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
            using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
            {
                swEncrypt.Write(plainText);
                Console.WriteLine("good");
                swEncrypt.Close();
                return msEncrypt.ToArray();
            }
        }
    }

    public static string Encrypt(string input, string key)
    {
        using (DESCryptoServiceProvider des = new DESCryptoServiceProvider())
        {
            byte[] textBytes = Encoding.UTF8.GetBytes(input);
            byte[] keyBytes = Encoding.UTF8.GetBytes(key);

            des.Mode = CipherMode.ECB; // Electronic Codebook

            using (MemoryStream ms = new MemoryStream())
            {
                using (CryptoStream cs = new CryptoStream(ms, des.CreateEncryptor(keyBytes, null), CryptoStreamMode.Write))
                {
                    cs.Write(textBytes, 0, textBytes.Length);
                    cs.FlushFinalBlock();
                    cs.Close();
                }
                string encryptedText = Convert.ToBase64String(ms.ToArray());
                return encryptedText;
            }
        }
    }


    public static string Decrypt(string encryptedInput, string key)
    {
        using (DESCryptoServiceProvider des = new DESCryptoServiceProvider())
        {
            byte[] encryptedTextBytes = Convert.FromBase64String(encryptedInput);
            byte[] keyBytes = Encoding.UTF8.GetBytes(key);

            des.Mode = CipherMode.ECB; // Electronic Codebook

            using (MemoryStream ms = new MemoryStream())
            {
                using (CryptoStream cs = new CryptoStream(ms, des.CreateDecryptor(keyBytes, null), CryptoStreamMode.Write))
                {
                    cs.Write(encryptedTextBytes, 0, encryptedTextBytes.Length);
                    cs.FlushFinalBlock();
                    cs.Close();
                }
                string decryptedText = Encoding.UTF8.GetString(ms.ToArray());
                return decryptedText;
            }
        }
    }

}
